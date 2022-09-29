import unittest
from app.classes.graph_node import test_graph
from app.classes.spec.symboleo_spec import PAtom
from app.src.graph_builder import GraphBuilder

class GraphBuilderTests(unittest.TestCase):
    def setUp(self):
        self.sut = GraphBuilder()

    def test_graph_builder(self):
        test_list = list(test_graph.values())
        test_list.sort(key=lambda x: x.name)

        result = self.sut.build(PAtom)
        result.sort(key=lambda x: x.name)

        self.assertEqual(len(test_list), len(result))

        for i,x in enumerate(test_list):
            self.assertEqual(x, result[i])

if __name__ == '__main__':
    unittest.main()



 # compare
# from app.classes.graph_node import test_graph

# test_list = list(test_graph.values())

# # sort both by name
# test_list.sort(key=lambda x: x.name)
# result.sort(key=lambda x: x.name)

# print(len(test_list), len(result))

# for i,x in enumerate(test_list):
#     print(x.name, result[i].name, x == result[i])
