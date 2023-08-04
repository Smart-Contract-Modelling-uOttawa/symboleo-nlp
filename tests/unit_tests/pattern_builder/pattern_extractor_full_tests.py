import unittest
from unittest.mock import MagicMock

from app.classes.units.all_units import *
from app.classes.pattern_classes.all_pattern_classes import *

from app.src.pattern_builder.pattern_class_getter import AllPatternClassGetter
from app.src.pattern_builder.single_pattern_checker import SinglePatternChecker
from app.src.pattern_builder.recursive_pattern_checker import RecursivePatternChecker
from app.src.pattern_builder.pattern_class_extractor import PatternClassExtractor

def mock_timespan():
    return [
        UnitType.TIMESPAN,
        UnitType.TIME_VALUE,
        UnitType.TIME_UNIT
    ]

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
    (
        [UnitType.AFTER] + mock_event(),
        AfterEvent
    ),
    (   
        [UnitType.FOLLOWING] + mock_timespan() + [UnitType.FOLLOWING] + mock_event(),
        AfterTimespanAfterEvent
    ),
    (   
        [UnitType.FOLLOWING] + mock_timespan() + [UnitType.BEFORE] + mock_event(),
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
    (
        [ UnitType.FOR] + mock_timespan() + [UnitType.FOLLOWING, UnitType.TIMEPOINT ], 
        ForTimespanInterval
    ),
    (
        [ UnitType.BETWEEN, UnitType.TIMEPOINT, UnitType.AND, UnitType.TIMEPOINT ], 
        BetweenInterval
    ),
    (
        [ UnitType.DURING, UnitType.TIME_PERIOD ], 
        DuringTimePeriod
    ),
    (
        [ UnitType.FROM, UnitType.TIMEPOINT, UnitType.UNTIL, UnitType.TIMEPOINT ], 
        FromUntilInterval
    ),
    (
        [ UnitType.UPON] + mock_timespan() + [UnitType.NOTICE_EVENT, UnitType.NOTICE_FROM, UnitType.NOTIFIER ], 
        NoticeEvent
    ),
    (
        mock_timespan() + [UnitType.BEFORE ] + mock_event(), 
        TimespanBeforeEvent
    ),
    (
        mock_timespan() + [UnitType.AFTER ] + mock_event3(), 
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
        [ UnitType.WITHIN] + mock_timespan() + [UnitType.OF] + mock_event(), 
        WithinTimespanEvent
    )
]

class PatternExtractorTests(unittest.TestCase):
    def setUp(self):
        self.getter = AllPatternClassGetter()

        recursive_checker = RecursivePatternChecker()
        single_checker = SinglePatternChecker(recursive_checker)
        self.sut = PatternClassExtractor(self.getter, single_checker)

    @unittest.skip('FIX')
    def test_update_processor(self):
        for test_val, exp_res in test_suite:
            result = self.sut.extract(test_val)
            self.assertTrue(exp_res in [type(x) for x in result])

if __name__ == '__main__':
    unittest.main()
