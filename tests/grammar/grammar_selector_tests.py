import unittest
from unittest.mock import MagicMock

from app.classes.tokens.abstract_node import DummyNode as DummyGrammarNode
from app.src.grammar.grammar_selector import GrammarSelector, ISelectGrammarNodes

from tests.helpers.test_grammar import TestGrammar

class GrammarSelectorTests(unittest.TestCase):
    def setUp(self):
        self.fake_node_selector = ISelectGrammarNodes()
        self.fake_node_selector.select = MagicMock(side_effect=[
            DummyGrammarNode('L1', [DummyGrammarNode('L2')]),
            DummyGrammarNode('L2'),
        ])
        self.sut = GrammarSelector(self.fake_node_selector)

    def test_grammar_selector(self):
        fake_grammar = TestGrammar.get_grammar()
        result = self.sut.select(fake_grammar)

        self.assertEqual(result.to_obj(None), 'dummy')
        self.assertEqual(self.fake_node_selector.select.call_count, 2)


if __name__ == '__main__':
    unittest.main()