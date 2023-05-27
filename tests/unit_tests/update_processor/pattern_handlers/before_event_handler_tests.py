import unittest
from unittest.mock import MagicMock

from app.classes.frames.before_event_frame import BeforeEventFrame
from app.classes.spec.norm import Norm, NormType
from app.classes.spec.prop_maker import PropMaker

from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.predicate_function import PredicateFunctionHappens

from app.src.update_processor.pattern_handlers.handle_object import HandleObject
from app.src.update_processor.pattern_handlers.before_event_handler import BeforeEventHandler

from tests.helpers.test_objects import CustomEvents

class BeforeEventHandlerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = BeforeEventHandler()

    def test_handler(self):
        norm = Norm('test', None, 'partyA', 'partyB', PropMaker.make_default(),
            PropMaker.make(PredicateFunctionHappens(VariableEvent('evt_a'))), NormType.Obligation)
        
        frame = BeforeEventFrame()
        frame.event = CustomEvents.paying()

        handle_object = HandleObject(
            norm = norm
        )

        result = self.sut.handle(frame, handle_object)
        new_norm = result[0]
        # TODO: Want a cleaner way of inspecting the consequent - convenience method...
        ## Maybe norm.get_predicate...
        exp_res = 'test: Obligation(partyA, partyB, true, WhappensBeforeE(evt_a, evt_pay));'
        
        self.assertEqual(len(result), 1)
        self.assertEqual(new_norm.to_sym(), exp_res)

if __name__ == '__main__':
    unittest.main()