"""Review invariants for Phase 3's original hypothetical examples and route boundaries."""
import json
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import manufacturing_map as graph

class DeviceWiringExamples(unittest.TestCase):
    def test_series_gate_capacitance_eot(self):
        eps0=8.8541878128e-12
        t=[.5e-9,2e-9];k=[3.9,20]
        eot=3.9*sum(a/b for a,b in zip(t,k))
        self.assertAlmostEqual(eot/1e-9,.89)
        series=1/sum(a/(eps0*b) for a,b in zip(t,k))
        self.assertAlmostEqual(series,eps0*3.9/eot)
        self.assertGreater(eot,2e-9*3.9/20)

    def test_sheet_perimeter_and_clearance(self):
        self.assertEqual(2*3*(30+5),210)
        self.assertEqual(12-2*3,6)
        self.assertEqual(12-2*6,0)
        self.assertLess(12-2*7,0)  # impossible residual gap in this ideal geometry

    def test_contact_area_units_and_shrink(self):
        side_cm=40e-7
        area=side_cm**2
        rc=1e-8/area
        self.assertAlmostEqual(rc,625)
        self.assertAlmostEqual(1e-8/(side_cm/2)**2,4*rc)
        self.assertAlmostEqual((8/10)**2,.64)
        self.assertAlmostEqual(1/.64,1.5625)

    def test_wire_units_delay_and_length_scaling(self):
        rho,length,width,height=3e-8,10e-6,40e-9,80e-9
        resistance=rho*length/(width*height)
        capacitance=.20e-15*(length/1e-6)
        self.assertAlmostEqual(resistance,93.75)
        tau=resistance*capacitance/2
        self.assertAlmostEqual(tau/1e-15,93.75)
        self.assertAlmostEqual((2*resistance)*(2*capacitance)/2,4*tau)
        loaded=500*(capacitance+3e-15)+resistance*(capacitance/2+3e-15)
        self.assertAlmostEqual(loaded/1e-12,2.875)

    def test_distributed_ladder_converges_to_first_moment(self):
        # N right-shunt RC segments approach the continuum RC/2 first moment.
        R,C=93.75,2e-15
        def first_moment(n):
            return sum((R/n)*(C/n)*(n-i) for i in range(n))
        target=R*C/2
        self.assertGreater(first_moment(10),target)
        self.assertLess(abs(first_moment(1000)-target),abs(first_moment(10)-target))
        self.assertAlmostEqual(first_moment(1000)/target,1.001)

    def test_power_and_current_density_units(self):
        current,resistance=100e-6,93.75
        self.assertAlmostEqual(current*resistance*1e3,9.375)
        self.assertAlmostEqual(current**2*resistance*1e6,.9375)
        j=1e-3/(40e-9*80e-9)
        self.assertAlmostEqual(j/1e11,3.125)
        self.assertAlmostEqual(j/1e4/1e7,3.125) # m² -> cm²

    def test_landing_geometry(self):
        nominal=(40-20)/2
        left,right=nominal-8,nominal+8
        self.assertEqual((left,right),(2,18))
        self.assertEqual(left+20+right,40)
        self.assertLess(left,4)
        self.assertGreater(left,0)  # overlap alone is insufficient for enclosure rule

    def test_teaching_routes_preserve_test_boundary(self):
        data=graph.read_data()
        routes={'ROUTE-PLANAR-TEACHING','ROUTE-FIN-TEACHING','ROUTE-SHEETS-TEACHING','ROUTE-MOL-TEACHING','ROUTE-BEOL-TEACHING'}
        edges=[e for e in data['process_edges'] if e['route_id'] in routes]
        reached=graph.reachable(graph.material_graph(edges),'MAT-0010')
        self.assertIn('ART-0214',reached)
        self.assertNotIn('ART-0030',reached) # tested logic die is deliberately outside these routes
        entities={e['entity_id']:e for e in data['entities']}
        self.assertEqual(entities['ART-0030']['status'],'planned')
        self.assertEqual(entities['PROC-0030']['status'],'planned')
        for rid in list(routes)[:]:
            if rid in {'ROUTE-MOL-TEACHING','ROUTE-BEOL-TEACHING'}:continue
            only=[e for e in edges if e['route_id']==rid]
            self.assertIn('ART-0200',graph.reachable(graph.material_graph(only),'MAT-0010'))

if __name__=='__main__':unittest.main()
