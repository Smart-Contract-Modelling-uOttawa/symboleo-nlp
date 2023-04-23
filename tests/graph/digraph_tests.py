import unittest
from tests.helpers.test_graph import TestGraph

class DigraphTests(unittest.TestCase):
    def setUp(self):
        self.sut = TestGraph.get_digraph()

    @unittest.skip('reorg')
    def test_digraph(self):
        node_a = self.sut.get_node('a')
        self.assertEqual(node_a.node_type, 'ROOT')
        self.assertEqual(len(node_a.subclasses), 2)
        self.assertEqual(len(node_a.props), 0)

        test_leaf_a = self.sut.is_leaf('a')
        self.assertFalse(test_leaf_a)

        test_leaf_f = self.sut.is_leaf('f')
        self.assertTrue(test_leaf_f)

        leaves = self.sut.leaves()
        self.assertEqual(len(leaves), 3)

        a_s_a = self.sut.is_subclass('a', 'a')
        self.assertTrue(a_s_a)

        b_s_a = self.sut.is_subclass('b', 'a')
        self.assertTrue(b_s_a)

        d_s_a = self.sut.is_subclass('d', 'a')
        self.assertTrue(d_s_a)

        # a_s_b = self.sut.is_subclass('a', 'b')
        # self.assertFalse(a_s_b)

if __name__ == '__main__':
    unittest.main()


