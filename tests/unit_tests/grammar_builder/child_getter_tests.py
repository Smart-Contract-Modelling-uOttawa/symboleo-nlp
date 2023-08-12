import unittest
from unittest.mock import MagicMock

from app.classes.grammar.grammar_node import GrammarNode
from app.classes.units.unit_type import UnitType
from app.classes.units.input_unit import InputUnit
from app.classes.pattern_classes.all_pattern_classes import *
from app.src.grammar_builder.grammar_builder import GrammarBuilder
from app.src.grammar_builder.pattern_tree_builder import IBuildPatternTrees
from app.src.grammar_builder.tree_merger import IMergeTrees

from app.src.grammar_builder.child_getter import ChildGetter
from app.src.grammar_builder.unit_builders.unit_builder import IBuildUnit

class ChildGetterTests(unittest.TestCase):
    def setUp(self):
        self.fake_builder = IBuildUnit()
        fake_dict = {
            UnitType.DUMMY: self.fake_builder
        }

        self.sut = ChildGetter(fake_dict)


    def test_child_getter(self):
        self.fake_builder.build = MagicMock(return_value=InputUnit())

        grammar_node = GrammarNode('TEST', [
            GrammarNode(UnitType.DUMMY.name)
        ])
        result = self.sut.get(grammar_node, None)

        self.assertEqual(len(result), 1)
        self.assertEqual(self.fake_builder.build.call_count, 1)
        

        


if __name__ == '__main__':
    unittest.main()
