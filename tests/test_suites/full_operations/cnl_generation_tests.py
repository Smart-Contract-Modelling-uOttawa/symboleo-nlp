import unittest
from unittest.mock import MagicMock
from typing import List
from app.classes.units.all_units import *
from app.classes.operations.user_input import UserInput
from app.classes.pattern_classes.all_pattern_classes import *

from app.src.pattern_builder.pattern_class_getter import AllPatternClassGetter
from app.src.pattern_builder.single_pattern_checker2 import SinglePatternChecker2
from app.src.pattern_builder.recursive_pattern_checker import RecursivePatternChecker
from app.classes.grammar.grammar_node import GrammarNode
from app.src.pattern_builder.pattern_class_extractor import PatternClassExtractor

from app.src.grammar_builder.grammar_builder_constructor import GrammarBuilderConstructor
from app.src.grammar_builder.grammar_builder import GrammarBuilder
from app.src.grammar_builder.child_getter import ChildGetter

from app.src.grammar_builder.unit_builders.unit_builder_dict import UnitBuilderDictConstructor

from tests.helpers.test_contract import get_test_contract

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
        [ UnitType.FOR] + mock_timespan() + [UnitType.AFTER, UnitType.EVENT ], 
        ForTimespanInterval
    ),
    (
        [ UnitType.BETWEEN, UnitType.DATE, UnitType.AND, UnitType.DATE ], 
        BetweenInterval
    ),
    (
        [ UnitType.DURING, UnitType.TIME_PERIOD ], 
        DuringTimePeriod
    ),
    (
        [UnitType.AT_LEAST] + mock_timespan() + [UnitType.BEFORE ] + mock_event(), 
        TimespanBeforeEvent
    ),
    (
        [UnitType.AT_LEAST] + mock_timespan() + [UnitType.AFTER ] + mock_event3(), 
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
    ),
    (
        [UnitType.UPON] + mock_timespan() + [ UnitType.NOTICE_EVENT, UnitType.NOTICE_FROM, UnitType.NOTIFIER], 
        NoticeEvent
    )
]

# Tests generation of all pattern classes
class PatternExtractorTests(unittest.TestCase):
    def setUp(self):
        self.pc_getter = AllPatternClassGetter()
        self.grammar_builder = GrammarBuilderConstructor.construct()

        recursive_checker = RecursivePatternChecker()
        single_checker = SinglePatternChecker2(recursive_checker)
        self.pc_extractor = PatternClassExtractor(self.pc_getter, single_checker)
        
        unit_dict = UnitBuilderDictConstructor.build()
        self.child_getter = ChildGetter(unit_dict)


    def test_cnl_generation(self):
        for test_list, exp_pc in test_suite:
            pattern_classes = self.pc_getter.get()
            curr_node = self.grammar_builder.build(pattern_classes)
            contract = get_test_contract()
            i = 0
            
            while i < len(test_list):
                input_list = self.child_getter.get(curr_node, contract)
                next_input = [x for x in input_list if x.unit_type == test_list[i]][0]
                curr_node = [x for x in curr_node.children if x.name == next_input.unit_type.value][0]
                i += 1
            
            user_inputs = [UserInput(x) for x in test_list]
            result = self.pc_extractor.extract(user_inputs)
            self.assertTrue(exp_pc in [type(x) for x in result])



if __name__ == '__main__':
    unittest.main()
