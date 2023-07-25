import unittest
from unittest.mock import MagicMock

from app.classes.units.all_units import *
from app.classes.pattern_classes.all_pattern_classes import *
from app.classes.pattern_classes.pattern_variables import PatternVariable as PV

from app.src.pattern_builder.recursive_pattern_checker import ICheckRecursivePattern
from app.src.pattern_builder.single_pattern_checker import SinglePatternChecker

class SinglePatternCheckerTests(unittest.TestCase):
    def setUp(self):
        self.recursive_checker = ICheckRecursivePattern()
        self.sut = SinglePatternChecker(self.recursive_checker)

    def test_single_pattern_checker_short(self):
        self.recursive_checker.check = MagicMock(side_effect=[(True, 0), (True, 0)])
        result = self.sut.check([UnitType.DUMMY], [PV.DATE, PV.DATE])

        self.assertFalse(result)
        self.assertEqual(self.recursive_checker.check.call_count, 0)
    

    def test_single_pattern_checker_pass(self):
        self.recursive_checker.check = MagicMock(side_effect=[(True, 0), (True, 0)])
        result = self.sut.check([UnitType.DUMMY, UnitType.DUMMY, UnitType.DUMMY], [PV.DATE, PV.DATE])

        self.assertTrue(result)
        self.assertEqual(self.recursive_checker.check.call_count, 2)


    def test_single_pattern_checker_fail(self):
        self.recursive_checker.check = MagicMock(side_effect=[(True, 0), (False, 0)])
        result = self.sut.check([UnitType.DUMMY, UnitType.DUMMY, UnitType.DUMMY], [PV.DATE, PV.DATE])

        self.assertFalse(result)
        self.assertEqual(self.recursive_checker.check.call_count, 2)
    



if __name__ == '__main__':
    unittest.main()
