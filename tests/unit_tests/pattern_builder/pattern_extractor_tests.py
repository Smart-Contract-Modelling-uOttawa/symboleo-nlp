import unittest
from unittest.mock import MagicMock

from app.classes.units.all_units import *
from app.classes.patterns.pattern_classes import *

from app.src.pattern_builder.pattern_class_getter import AllPatternClassGetter
from app.src.pattern_builder.pattern_class_extractor import PatternClassExtractor

test_suite = [
    (
        [
            UnitType.BEFORE,
            UnitType.DATE,
        ], 
        BeforeDate
    ),
    (
        [
            UnitType.WITHIN,
            UnitType.TIMESPAN,
            UnitType.OF,
            UnitType.EVENT,
        ], 
        WithinTimespanEvent
    ),
    (
        [
            UnitType.UNLESS,
            UnitType.EVENT,
            UnitType.CUSTOM_EVENT,
            UnitType.SUBJECT,
            UnitType.TRANSITIVE_VERB,
            UnitType.DOBJ,
            UnitType.PREP_PHRASE,
        ], 
        ExceptEvent
    ),
]

# TODO: Add all test cases
class PatternExtractorTests(unittest.TestCase):
    def setUp(self):
        self.getter = AllPatternClassGetter()
        self.sut = PatternClassExtractor(self.getter)


    def test_update_processor(self):
        for test_val, exp_res in test_suite:
            result = self.sut.extract(test_val)

            self.assertTrue(isinstance(result, exp_res))

if __name__ == '__main__':
    unittest.main()
