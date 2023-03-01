import unittest
import copy
from app.classes.spec.proposition import PAtom
from app.src.graph.graph_builder import GraphBuilder
from app.classes.graph.graph_node import test_graph

class GraphBuilderTests(unittest.TestCase):
    def setUp(self):
        self.sut = GraphBuilder()

    def test_graph_builder(self):
        test_list = list(test_graph.values())
        test_list.sort(key=lambda x: x.name)

        result = self.sut.build(PAtom)
        result_nodes = copy.deepcopy(result.nodes)
        result_nodes.sort(key=lambda x: x.name)

        self.assertEqual(len(test_list), len(result_nodes))

        for i,x in enumerate(test_list):
            self.assertEqual(x, result_nodes[i])

if __name__ == '__main__':
    unittest.main()


