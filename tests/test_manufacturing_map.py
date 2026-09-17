"""Regression checks for graph errors that could silently corrupt navigation."""
import copy
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import manufacturing_map as graph

class GraphIntegrity(unittest.TestCase):
    def setUp(self):self.data=copy.deepcopy(graph.read_data())
    def test_real_graph_valid(self):self.assertEqual(graph.validate(self.data),[])
    def test_dangling_endpoint_rejected(self):
        self.data['process_edges'][0]['target_id']='NO-SUCH-ENTITY'
        self.assertTrue(any('Dangling' in e for e in graph.validate(self.data)))
    def test_missing_evidence_rejected(self):
        self.data['evidence_links']=[]
        self.data['process_edges'][0]['status']='reviewed'
        self.assertTrue(any('No edge evidence' in e for e in graph.validate(self.data)))
    def test_wrong_endpoint_type_rejected(self):
        self.data['process_edges'][0]['relationship']='SUPPLIED_BY'
        self.assertTrue(any('Wrong endpoint' in e for e in graph.validate(self.data)))
    def test_sequence_cycle_rejected(self):
        self.assertTrue(graph.has_cycle([('a','b'),('b','c'),('c','a')]))
        self.assertFalse(graph.has_cycle([('a','b'),('a','c'),('b','d'),('c','d')]))
    def test_projection_stops_at_next_retained_node(self):
        adj=graph.defaultdict(set,{'a':{'b'},'b':{'c'},'c':{'d'}})
        self.assertEqual(graph.reachable(adj,'a',{'b','d'}),{'b'})
    def test_material_conversion_direction(self):
        edges=[{'source_id':'op','relationship':'CONSUMES','target_id':'in'},{'source_id':'op','relationship':'PRODUCES','target_id':'out'}]
        adj=graph.material_graph(edges)
        self.assertIn('out',graph.reachable(adj,'in'))
        self.assertNotIn('in',graph.reachable(adj,'out'))
if __name__=='__main__':unittest.main()
