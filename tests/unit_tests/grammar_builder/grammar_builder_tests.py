import unittest
from unittest.mock import MagicMock

from app.classes.grammar.grammar_node import GrammarNode
from app.classes.pattern_classes.all_pattern_classes import *
from app.src.grammar_builder.grammar_builder import GrammarBuilder
from app.src.grammar_builder.pattern_tree_builder import IBuildPatternTrees
from app.src.grammar_builder.tree_merger import IMergeTrees


class GrammarBuilderTests(unittest.TestCase):
    def setUp(self):
        self.fake_tree_builder = IBuildPatternTrees()
        self.fake_tree_builder.build = MagicMock(return_value = [GrammarNode('XXX')])

        self.fake_merger = IMergeTrees()
        self.fake_merger.merge = MagicMock(return_value = None)

        self.sut = GrammarBuilder(self.fake_tree_builder, self.fake_merger)


    def test_grammar_builder(self):
        p = BeforeDate()
        result = self.sut.build([p])
        
        exp_value = GrammarNode('ROOT')
        self.assertEqual(result, exp_value)
        self.assertEqual(self.fake_merger.merge.call_count, 1)
        self.assertEqual(self.fake_tree_builder.build.call_count, 1)

        


if __name__ == '__main__':
    unittest.main()
