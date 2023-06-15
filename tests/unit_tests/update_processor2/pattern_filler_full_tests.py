import unittest
from unittest.mock import MagicMock

from app.classes.spec.sym_event import VariableEvent
from app.classes.operations.user_input import UnitType, UserInput
from app.classes.units.all_units import *
from app.classes.patterns.pattern_classes import *

from app.src.update_processor2.pattern_unit_fillers.pattern_unit_filler_dict import PatternUnitFillerDictConstructor
from app.src.update_processor2.pattern_class_filler import PatternClassFiller

test_suite = [
    (
        [
            UnitType.BEFORE,
            UnitType.DATE,
        ], 
        BeforeDate()
    ),
    (
        [
            UnitType.WITHIN,
            UnitType.TIMESPAN,
            UnitType.OF,
            UnitType.EVENT,
        ], 
        WithinTimespanEvent()
    ),
]

class PatternExtractorTests(unittest.TestCase):
    def setUp(self):
        self.dict = PatternUnitFillerDictConstructor.build()
        self.sut = PatternClassFiller(self.dict)


    def test_update_processor(self):
        input_list = [
            UserInput(UnitType.WITHIN),
            UserInput(UnitType.TIMESPAN, '3 weeks'),
            UserInput(UnitType.OF),
            UserInput(UnitType.EVENT),
            UserInput(UnitType.CUSTOM_EVENT, 'evt_test')
        ] 

        pattern_class = WithinTimespanEvent()

        result = self.sut.fill(pattern_class, input_list)

    
        self.assertTrue(isinstance(result, WithinTimespanEvent))
        res:WithinTimespanEvent = result

        self.assertEqual(res.event, VariableEvent('evt_test'))
        self.assertEqual(res.timespan_value, '3')
        self.assertEqual(res.timespan_unit, 'weeks')

if __name__ == '__main__':
    unittest.main()
