import unittest
from unittest.mock import MagicMock

from app.classes.units.all_units import *
from app.classes.pattern_classes.all_pattern_classes import *

from app.src.pattern_builder.pattern_class_getter import IGetAllPatternClasses
from app.src.pattern_builder.single_pattern_checker import ICheckSinglePattern
from app.src.pattern_builder.pattern_class_extractor import PatternClassExtractor

class PatternExtractorTests(unittest.TestCase):
    def setUp(self):
        self.getter = IGetAllPatternClasses()
        self.getter.get = MagicMock(return_value = [BeforeDate, BeforeEvent])
        self.single_checker = ICheckSinglePattern()
        self.single_checker.check = MagicMock(side_effect=[BeforeDate(), None])
        self.sut = PatternClassExtractor(self.getter, self.single_checker)

    def test_pattern_extractor(self):
        result = self.sut.extract([UnitType.DUMMY])

        self.assertEqual(len(result), 1)
        self.assertEqual(type(result[0]), BeforeDate)
        self.assertEqual(self.getter.get.call_count, 1)
        self.assertEqual(self.single_checker.check.call_count, 2)
    

if __name__ == '__main__':
    unittest.main()
