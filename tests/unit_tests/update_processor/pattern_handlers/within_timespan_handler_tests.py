import unittest
from unittest.mock import MagicMock

from app.classes.patterns.within_timespan_event import WithinTimespanEvent
from app.classes.spec.norm import Norm, NormType
from app.classes.spec.prop_maker import PropMaker
from app.classes.other.timespan import Timespan
from app.classes.spec.point_function import TimeUnit
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.predicate_function import PredicateFunctionHappens

from app.src.update_processor.pattern_handlers.handle_object import HandleObject
from app.src.update_processor.pattern_handlers.within_timespan_handler import WithinTimespanHandler

from tests.helpers.test_objects import CustomEvents

class WithinTimespanHandlerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = WithinTimespanHandler()

    def test_handler(self):
        norm = Norm('test', None, 'partyA', 'partyB', PropMaker.make_default(),
            PropMaker.make(PredicateFunctionHappens(VariableEvent('evt_a'))), NormType.Obligation)
        
        pattern = WithinTimespanEvent()
        pattern.event = CustomEvents.paying()
        pattern.timespan = Timespan('2', TimeUnit.Days)

        handle_object = HandleObject(
            norm = norm
        )

        result = self.sut.handle(pattern, handle_object)
        new_norm = result[0]
        exp_res = 'test: Obligation(partyA, partyB, true, WhappensBefore(evt_a, Date.Add(evt_pay, 2, days)));'
        
        self.assertEqual(len(result), 1)
        self.assertEqual(new_norm.to_sym(), exp_res)

if __name__ == '__main__':
    unittest.main()