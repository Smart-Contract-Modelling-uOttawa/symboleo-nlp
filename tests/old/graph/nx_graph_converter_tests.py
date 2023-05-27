import unittest
from app.classes.graph.graph_node import GraphNode
from app.classes.graph.digraph import Digraph

class NxGraphConverterTests(unittest.TestCase):
    def setUp(self):
        graph_nodes = [
            GraphNode('a', 'x', ['b', 'c'], []),
            GraphNode('b', 'x', [], ['d']),
            GraphNode('c', 'x', [], ['d'])
        ]
        self.sut = Digraph(graph_nodes)

    def test_path_dict_builder(self):
        result = self.sut.get_nx_graph()
        self.assertEqual(list(result.nodes), ['a', 'b', 'c', 'd'])
        self.assertEqual(list(result.edges), [('a', 'b'), ('a', 'c'), ('b', 'd'), ('c', 'd')])

if __name__ == '__main__':
    unittest.main()