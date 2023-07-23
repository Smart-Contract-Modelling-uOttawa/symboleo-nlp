import unittest
from unittest.mock import MagicMock

from app.classes.units.all_units import *
from app.classes.pattern_classes.all_pattern_classes import *

from app.src.pattern_builder.pattern_class_getter import IGetAllPatternClasses
from app.src.pattern_builder.pattern_class_extractor import PatternClassExtractor


def mock_event():
    return [
        UnitType.EVENT, 
        UnitType.CUSTOM_EVENT, 
        UnitType.SUBJECT,
        UnitType.TRANSITIVE_VERB,
        UnitType.DOBJ, 
        UnitType.PREP_PHRASE
    ]

def mock_event2():
    return [
        UnitType.EVENT,
        UnitType.CONTRACT_EVENT,
        UnitType.CONTRACT_SUBJECT,
        UnitType.CONTRACT_ACTION
    ]

def mock_event3():
    return [
        UnitType.EVENT,
        UnitType.CUSTOM_EVENT,
        UnitType.SUBJECT,
        UnitType.TRANSITIVE_VERB,
        UnitType.DOBJ
    ]

# Want a test for each pattern class
test_suite = [
    (
        [ UnitType.FROM, UnitType.TIMEPOINT, UnitType.UNTIL, UnitType.TIMEPOINT ], 
        FromUntilInterval
    )
]

# TODO: Add all test cases
class PatternExtractorTests(unittest.TestCase):
    def setUp(self):
        self.getter = IGetAllPatternClasses()
        self.getter.get = MagicMock(return_value = [
            FromUntilInterval()
        ])
        self.sut = PatternClassExtractor(self.getter)


    def test_update_processor(self):
        for test_val, exp_res in test_suite:
            result = self.sut.extract(test_val)

            self.assertTrue(isinstance(result[0], exp_res))

if __name__ == '__main__':
    unittest.main()
