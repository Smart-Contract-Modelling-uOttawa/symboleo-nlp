import unittest
from unittest.mock import MagicMock

from app.classes.units.all_units import *
from app.classes.operations.user_input import UserInput
from app.classes.pattern_classes.pattern_class import PatternClass
from app.classes.pattern_classes.all_pattern_classes import *
from app.classes.pattern_classes.pattern_variables import PatternVariable as PV

from app.src.pattern_builder.pattern_class_getter import AllPatternClassGetter
from app.src.pattern_builder.single_pattern_checker import SinglePatternChecker
from app.src.pattern_builder.recursive_pattern_checker import ICheckRecursivePattern


class TestClass1(PatternClass):
    sequence = [PV.DUMMY, PV.DUMMY]

class TestClass2(PatternClass):
    sequence = [PV.DUMMY]


class SinglePatternCheckerTests(unittest.TestCase):
    def setUp(self):
        self.getter = AllPatternClassGetter()

        self.recursive_checker = ICheckRecursivePattern()
        self.sut = SinglePatternChecker(self.recursive_checker, {
            PV.DUMMY: UnitType.DUMMY
        })

    def test_single_pattern_checker1(self):
        set_to_check = [UserInput(UnitType.DUMMY)]
        result = self.sut.check(set_to_check, TestClass1)

        self.assertIsNone(result)


    def test_single_pattern_checker2(self):
        self.recursive_checker.check = MagicMock(return_value=(False,1))

        set_to_check = [UserInput(UnitType.DUMMY)]
        result = self.sut.check(set_to_check, TestClass2)

        self.assertIsNone(result)
    
    def test_single_pattern_checker3(self):
        self.recursive_checker.check = MagicMock(return_value=(True,1))

        set_to_check = [UserInput(UnitType.DUMMY, 'test')]
        result = self.sut.check(set_to_check, TestClass2)

        self.assertEqual(type(result), TestClass2)
        self.assertEqual(result.val_dict, {PV.DUMMY: 'test'})


if __name__ == '__main__':
    unittest.main()
