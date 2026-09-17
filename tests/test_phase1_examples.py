"""Independent arithmetic and physical invariants for the published teaching examples.

All inputs are hypothetical unless the owning chapter identifies a teaching constant.
These checks validate arithmetic/model consistency, never production suitability.
"""
import math
import unittest

class FoundationExamples(unittest.TestCase):
    def test_grade_recovery_and_mass_balance(self):
        feed,feed_grade,product,product_grade=100.,.95,90.,.99
        retained=product*product_grade
        self.assertAlmostEqual(100*retained/(feed*feed_grade),93.7894736842)
        self.assertNotEqual(product_grade,retained/(feed*feed_grade))
        self.assertLessEqual(retained,feed*feed_grade)
        self.assertAlmostEqual(product/feed,.9)

    def test_reduction_stoichiometry(self):
        # SiO2 + 2 C -> Si + 2 CO: elemental conservation and rounded molar masses.
        self.assertAlmostEqual(60.1+2*12.,28.1+2*28.)
        self.assertAlmostEqual(60.1/28.1,2.14,places=2)
        self.assertAlmostEqual(24/28.1,.854,places=3)

    def test_mass_denominator_and_impurity_units(self):
        self.assertAlmostEqual(1000/80,12.5)
        self.assertAlmostEqual(1000/70,14.3,places=1)
        self.assertGreater(1000/70,1000/80)
        self.assertAlmostEqual(1e-9*5e22,5e13,delta=1.)
        self.assertEqual(.5*2e16,1e16)
        self.assertEqual(1e10*.02,2e8)

    def test_wafer_geometry(self):
        self.assertEqual(math.floor(1000/(.9+.1)),1000)
        self.assertAlmostEqual(math.pi*(300/2-3)**2,67887,delta=1)
        self.assertAlmostEqual((147/150)**2,.9604)
        self.assertLess((147/150)**2,1)

    def test_neutrality_transport_and_unit_conversion(self):
        donors,acceptors,ni=1.2e16,2e15,1e10
        net=donors-acceptors
        # Exact positive quadratic root, independent of the chapter's majority approximation.
        n=.5*(net+math.sqrt(net*net+4*ni*ni)); p=ni*ni/n
        self.assertAlmostEqual(n/net,1.,places=10)
        self.assertAlmostEqual(p,1e4,places=5)
        self.assertAlmostEqual((n+acceptors)/(p+donors),1.,places=12)
        sigma_cm=1.60e-19*n*1000
        sigma_m=1.60e-19*(n*1e6)*(1000*1e-4)
        self.assertAlmostEqual(sigma_m/sigma_cm,100)
        self.assertAlmostEqual(1/sigma_cm,.625,places=10)
        self.assertAlmostEqual(.625*.1/.01,6.25)

    def test_junction_potential_and_charge_balance(self):
        self.assertAlmostEqual(.02585*math.log(1e16*1e16/1e20),.714,places=3)
        # A tenfold n-side doping needs a tenfold narrower depleted n-side width.
        self.assertAlmostEqual((1e16*1e-4)/(1e17*1e-5),1.,places=12)

    def test_gate_capacitance_and_mos_boundary(self):
        c_area=3.45e-11/4e-9
        self.assertAlmostEqual(c_area,.008625)
        self.assertAlmostEqual(c_area*1e-12/1e-15,8.625)
        beta,overdrive=1e-3,.4
        linear=lambda vd: beta*(overdrive*vd-vd*vd/2)
        saturation=beta*overdrive**2/2
        self.assertAlmostEqual(linear(.1)/1e-6,35.)
        self.assertAlmostEqual(saturation/1e-6,80.)
        self.assertAlmostEqual(linear(overdrive),saturation)
        self.assertEqual(linear(0),0.)

    def test_switching_time_and_energy(self):
        c,v,i,activity,f=10e-15,.8,100e-6,.1,1e9
        self.assertAlmostEqual(c*v/i/1e-12,80.)
        self.assertAlmostEqual(activity*c*v*v*f/1e-6,.64)
        self.assertAlmostEqual((2*c)*v/i,2*(c*v/i))

if __name__=='__main__':unittest.main()
