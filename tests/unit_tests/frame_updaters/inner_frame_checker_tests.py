
import unittest
from unittest.mock import MagicMock

from app.classes.patterns.all_patterns import *
from app.classes.units.unit_type import UnitType
from app.classes.elements.all_nodes import *
from app.src.pattern_updaters.inner_pattern_checker import InnerPatternChecker

class InnerPatternCheckerTests(unittest.TestCase):
    def setUp(self):
        self.sut = InnerPatternChecker()
    
    def test_inner_pattern_checker1(self):
        node_list = [RootNode(), BeforeNode(), EventNode(), CustomEventNode()]
        pattern_sequence = [UnitType.ROOT, UnitType.BEFORE, UnitType.EVENT]

        result = self.sut.check_pattern(node_list, pattern_sequence)
        self.assertTrue(result)
    
    def test_inner_pattern_checker2(self):
        node_list = [RootNode(), BeforeNode()]
        pattern_pattern = [UnitType.ROOT, UnitType.BEFORE, UnitType.EVENT]

        result = self.sut.check_pattern(node_list, pattern_pattern)
        self.assertFalse(result)

    def test_inner_pattern_checker1(self):
        node_list = [RootNode(), BeforeNode(), EventNode(), CustomEventNode()]
        pattern_pattern = [UnitType.ROOT, UnitType.AFTER, UnitType.EVENT]

        result = self.sut.check_pattern(node_list, pattern_pattern)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
