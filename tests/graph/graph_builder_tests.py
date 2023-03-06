import unittest
import copy
from app.classes.spec.p_atoms import PAtomPredicate
from app.src.old.graph.graph_builder import GraphBuilder
from app.classes.graph.graph_node import test_graph

class GraphBuilderTests(unittest.TestCase):
    def setUp(self):
        self.sut = GraphBuilder()

    def test_graph_builder(self):
        test_list = list(test_graph.values())
        test_list.sort(key=lambda x: x.name)

        result = self.sut.build(PAtomPredicate)
        result_nodes = copy.deepcopy(result.nodes)
        result_nodes.sort(key=lambda x: x.name)

        self.assertEqual(len(test_list), len(result_nodes))
        for i, x in enumerate(test_list):
            self.assertEqual(x, result_nodes[i], f'{x.name} != {result_nodes[i].name}')

if __name__ == '__main__':
    unittest.main()


