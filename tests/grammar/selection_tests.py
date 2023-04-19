import unittest
from unittest.mock import MagicMock

from app.classes.tokens.abstract_node import DummyNode as DummyGrammarNode
from app.classes.tokens.root_node import RootNode
from app.src.grammar.selection import Selection

class SelectionTests(unittest.TestCase):
    def setUp(self):
        self.sut = Selection()

    def test_selection(self):
        self.sut.add_node(RootNode('Root'))
        self.sut.add_node(DummyGrammarNode('a'), 'a')
        result = self.sut.get_update_obj()
        self.assertEqual(result, 'dummy')

if __name__ == '__main__':
    unittest.main()