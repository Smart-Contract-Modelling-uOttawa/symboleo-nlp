import unittest
from unittest.mock import MagicMock

from app.classes.grammar.grammar_node import GrammarNode
from app.src.grammar_builder.tree_printer import TreePrinter
from app.classes.pattern_classes.all_pattern_classes import *
from app.src.grammar_builder.pattern_tree_builder import PatternTreeBuilder

class PatternTreeBuilderTests(unittest.TestCase):
    def setUp(self):
        self.sut = PatternTreeBuilder()

    def test_pattern_tree_builder(self):
        p = BeforeDate()
        t_result = self.sut.build(p)
        
        result = GrammarNode('ROOT', t_result)


        #self.assertEqual(len(result), 2)

        exp_val = GrammarNode('ROOT', [
            GrammarNode('BEFORE', [ GrammarNode('DATE')]),
            GrammarNode('BY', [ GrammarNode('DATE')])
        ])
        self.assertEqual(result, exp_val)

        #self.assertEqual(len(result), 2)
        #self.assertEqual(result[0], exp1)
        #self.assertEqual(result[1], exp2)
        


if __name__ == '__main__':
    unittest.main()
