import unittest
from unittest.mock import MagicMock

from app.classes.grammar.grammar_node import GrammarNode
from app.classes.grammar.full_grammar import FULL_GRAMMAR
from app.classes.pattern_classes.pattern_class import PatternClass, PatternVariable as PV
from app.classes.pattern_classes.all_pattern_classes import *

from app.src.grammar_builder.pattern_tree_builder import PatternTreeBuilder
from app.src.grammar_builder.tree_printer import TreePrinter

# single unit
class TestClass1(PatternClass):
    sequence = [PV.WITHIN]

# GOr
class TestClass2(PatternClass):
    sequence = [PV.P_BEFORE_S]

# GAnd
class TestClass3(PatternClass):
    sequence = [PV.TIMESPAN]



class PatternTreeBuilderTests(unittest.TestCase):
    def setUp(self):
        self.sut = PatternTreeBuilder(FULL_GRAMMAR)

    def test_pattern_tree_builder1(self):
        a = TestClass1()
        t_res = self.sut.build(a)

        result = GrammarNode('ROOT', t_res)

        exp_val = GrammarNode('ROOT', [
            GrammarNode('WITHIN', [])
        ])
        self.assertEqual(result, exp_val)
    

    def test_pattern_tree_builder2(self):
        a = TestClass2()
        t_res = self.sut.build(a)

        result = GrammarNode('ROOT', t_res)

        exp_val = GrammarNode('ROOT', [
            GrammarNode('BEFORE', []),
            GrammarNode('BY', [])
        ])
        self.assertEqual(result, exp_val)
    

    def test_pattern_tree_builder3(self):
        a = TestClass3()
        t_res = self.sut.build(a)

        result = GrammarNode('ROOT', t_res)

        exp_val = GrammarNode('ROOT', [
            GrammarNode('TIMESPAN', [
                GrammarNode('TIME_VALUE', [
                    GrammarNode('TIME_UNIT', [])
                ]),
            ]),
        ])
        self.assertEqual(result, exp_val)


if __name__ == '__main__':
    unittest.main()
