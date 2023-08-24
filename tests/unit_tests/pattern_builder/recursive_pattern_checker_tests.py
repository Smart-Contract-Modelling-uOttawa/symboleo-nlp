import unittest
from unittest.mock import MagicMock

from app.classes.units.all_units import *
from app.classes.pattern_classes.all_pattern_classes import *
from app.classes.pattern_classes.pattern_variables import PatternVariable as PV
from app.classes.grammar.full_grammar import FULL_GRAMMAR, GOr, GAnd

from app.src.pattern_builder.recursive_pattern_checker import RecursivePatternChecker

# TODO: Add tests
class RecursivePatternCheckerTests(unittest.TestCase):
    def setUp(self):
        self.sut = RecursivePatternChecker(FULL_GRAMMAR)

    def test_recursive_pattern_checker_unit(self):
        units = [UnitType.DUMMY]
        ind = 0
        pattern_obj = UnitType.DUMMY
        result = self.sut.check(units, ind, pattern_obj)
        self.assertEqual(result, (True, 1))
    

    def test_recursive_pattern_checker_unit_f(self):
        units = [UnitType.DUMMY]
        ind = 0
        pattern_obj = UnitType.WITHIN
        result = self.sut.check(units, ind, pattern_obj)
        self.assertEqual(result, (False, 0))
    

    def test_recursive_pattern_checker_or(self):
        units = [UnitType.DUMMY]
        ind = 0
        pattern_obj = GOr(UnitType.DUMMY, UnitType.DUMMY)
        result = self.sut.check(units, ind, pattern_obj)
        self.assertEqual(result, (True, 1))
    

    def test_recursive_pattern_checker_or_f(self):
        units = [UnitType.WITHIN]
        ind = 0
        pattern_obj = GOr(UnitType.DUMMY, UnitType.DUMMY)
        result = self.sut.check(units, ind, pattern_obj)
        self.assertEqual(result, (False, 0))
    

    def test_recursive_pattern_checker_and(self):
        units = [UnitType.DUMMY]
        ind = 0
        pattern_obj = GAnd(UnitType.DUMMY, UnitType.DUMMY)
        result = self.sut.check(units, ind, pattern_obj)
        self.assertEqual(result, (True, 2))
    

    def test_recursive_pattern_checker_and_f(self):
        units = [UnitType.DUMMY]
        ind = 0
        pattern_obj = GAnd(UnitType.WITHIN, UnitType.DUMMY)
        result = self.sut.check(units, ind, pattern_obj)
        self.assertEqual(result, (False, 0))
    

    def test_recursive_pattern_checker_and_tf(self):
        units = [UnitType.DUMMY, UnitType.DUMMY]
        ind = 0
        pattern_obj = GAnd(UnitType.DUMMY, UnitType.WITHIN)
        result = self.sut.check(units, ind, pattern_obj)
        self.assertEqual(result, (False, 0))
    

    def test_recursive_pattern_checker_pv(self):
        units = [UnitType.WITHIN]
        ind = 0
        pattern_obj = PV.WITHIN
        result = self.sut.check(units, ind, pattern_obj)
        self.assertEqual(result, (True, 1))
    
    



if __name__ == '__main__':
    unittest.main()
