import unittest
from unittest.mock import MagicMock
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.sym_point import Point, PointVDE
from app.classes.pattern_classes.before_event import BeforeEvent
from app.classes.spec.predicate_function import PredicateFunctionWHappensBeforeEvent
from app.classes.operations.handle_object import HandleObject
from app.classes.helpers.prop_maker import PropMaker
from app.classes.spec.norm import Obligation

from app.src.norm_update_extractor.handlers.before_event_handler import BeforeEventHandler
from tests.helpers.sample_norm_lib import SampleNorms

class BeforeEventHandlerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = BeforeEventHandler()

    def test_handler(self):
        norm = SampleNorms.get_sample_obligation('test_id')
        pattern_class = BeforeEvent()
        pattern_class.event = VariableEvent('evt_test')
        handle_obj = HandleObject(norm)

        result = self.sut.handle(pattern_class, handle_obj)
        
        new_norm: Obligation = result[0]
        self.assertEqual(len(result), 1)

        exp_norm = Obligation(
            'test_id',
            None,
            'debtor',
            'creditor',
            PropMaker.make_default(),
            PropMaker.make(
                PredicateFunctionWHappensBeforeEvent(
                    VariableEvent('evt_action'),
                    VariableEvent('evt_test')
                )
            )
        )
        self.assertEqual(new_norm, exp_norm)

if __name__ == '__main__':
    unittest.main()