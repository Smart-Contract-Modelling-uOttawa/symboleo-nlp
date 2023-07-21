import unittest
from unittest.mock import MagicMock

from app.classes.units.all_units import *
from app.classes.pattern_classes.all_pattern_classes import *

from app.src.pattern_builder.pattern_class_getter import AllPatternClassGetter, IGetAllPatternClasses
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
        [UnitType.LATER_THAN, UnitType.DATE],
        AfterDate
    ),
    # TODO: This one is ambiguous!!! How to handle...?
    # (
    #     [UnitType.AFTER, UnitType.EVENT],
    #     AfterEvent
    # ),
    (   
        [UnitType.FOLLOWING, UnitType.TIMESPAN, UnitType.FOLLOWING] + mock_event(),
        AfterTimespanAfterEvent
    ),
    (   
        [UnitType.FOLLOWING, UnitType.TIMESPAN, UnitType.BEFORE] + mock_event(),
        AfterTimespanBeforeEvent
    ),
    (
        [ UnitType.BEFORE, UnitType.DATE], 
        BeforeDate
    ),
    (
        [ UnitType.PRIOR_TO] + mock_event(), 
        BeforeEvent
    ),
    (
        [ UnitType.IN_CASE] + mock_event2(), 
        CondAEvent
    ),
    (
        [ UnitType.WHEN ] + mock_event2(), 
        CondTEvent
    ),
    (
        [ UnitType.UNLESS] + mock_event(), 
        ExceptEvent
    ),
    # (
    #     mock_event() + [ UnitType.DURING, UnitType.TIME_PERIOD ], 
    #     EventInterval
    # ),
    # (
    #     mock_event2() + [ UnitType.BETWEEN, UnitType.TIMEPOINT, UnitType.AND, UnitType.TIMEPOINT ], 
    #     EventInterval
    # ),
    # (
    #     [ UnitType.BY_GIVING, UnitType.TIMESPAN, UnitType.NOTICE_EVENT ], 
    #     NoticeEvent
    # ),
    (
        [ UnitType.TIMESPAN, UnitType.BEFORE ] + mock_event(), 
        TimespanBeforeEvent
    ),
    (
        [ UnitType.TIMESPAN, UnitType.AFTER ] + mock_event(), 
        TimespanAfterEvent
    ),
    (
        [ UnitType.TIMESPAN, UnitType.AFTER ] + mock_event3(), 
        TimespanAfterEvent
    ),
    (
        [ UnitType.UNTIL, UnitType.DATE ], 
        UntilDate
    ),
    (
        [ UnitType.UNTIL ] + mock_event(), 
        UntilEvent
    ),
    (
        [ UnitType.WITHIN, UnitType.TIMESPAN, UnitType.OF] + mock_event(), 
        WithinTimespanEvent
    )
]

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
