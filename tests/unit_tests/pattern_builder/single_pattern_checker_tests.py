import unittest
from unittest.mock import MagicMock

from app.classes.units.all_units import *
from app.classes.operations.user_input import UserInput
from app.classes.pattern_classes.all_pattern_classes import *

from app.src.pattern_builder.pattern_class_getter import AllPatternClassGetter
from app.src.pattern_builder.single_pattern_checker import SinglePatternChecker
from app.src.pattern_builder.recursive_pattern_checker import RecursivePatternChecker
from app.src.pattern_builder.pattern_class_extractor import PatternClassExtractor

def mock_timespan():
    return [
        UserInput(UnitType.TIMESPAN),
        UserInput(UnitType.TIME_VALUE, '2'),
        UserInput(UnitType.TIME_UNIT, 'weeks')
    ]

def mock_event(verb = 'eats'):
    return [
        UserInput(UnitType.EVENT), 
        UserInput(UnitType.CUSTOM_EVENT), 
        UserInput(UnitType.SUBJECT, 'bob'),
        UserInput(UnitType.TRANSITIVE_VERB, verb),
        UserInput(UnitType.DOBJ, 'pie'), 
        UserInput(UnitType.PREP_PHRASE, 'with mary')
    ]

def mock_event2():
    return [
        UserInput(UnitType.EVENT),
        UserInput(UnitType.CONTRACT_EVENT),
        UserInput(UnitType.CONTRACT_SUBJECT, 'contract'),
        UserInput(UnitType.CONTRACT_ACTION, 'terminates')
    ]

def mock_event3(verb = 'eats'):
    return [
        UserInput(UnitType.EVENT),
        UserInput(UnitType.CUSTOM_EVENT),
        UserInput(UnitType.SUBJECT, 'bob'),
        UserInput(UnitType.TRANSITIVE_VERB, verb),
        UserInput(UnitType.DOBJ, 'pie')
    ]

# Want a test for each pattern class
test_suite = [
    (
        [ UserInput(UnitType.WITHIN, 'within')] + mock_timespan() + [UserInput(UnitType.OF, 'of')] + mock_event('eating'), 
        WithinTimespanEvent,
        'within 2 weeks of bob eating pie with mary'
    )
]

class PatternExtractorTests(unittest.TestCase):
    def setUp(self):
        self.getter = AllPatternClassGetter()

        recursive_checker = RecursivePatternChecker()
        self.sut = SinglePatternChecker(recursive_checker)


    def test_update_processor(self):
        for test_val, pc_type, exp_text in test_suite:
            result = self.sut.check(test_val, pc_type)

            self.assertEqual(type(result), pc_type)

            self.assertEqual(result.to_text(), exp_text)


if __name__ == '__main__':
    unittest.main()
