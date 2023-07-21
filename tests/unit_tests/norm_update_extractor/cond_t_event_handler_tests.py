import unittest
from unittest.mock import MagicMock
from app.classes.spec.sym_event import VariableEvent
from app.classes.pattern_classes.cond_t_event import CondTEvent
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.operations.handle_object import HandleObject
from app.classes.helpers.prop_maker import PropMaker
from app.classes.spec.norm import Obligation

from app.src.norm_update_extractor.handlers.cond_t_event_handler import CondTEventHandler
from tests.helpers.sample_norm_lib import SampleNorms

class CondTEventHandlerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = CondTEventHandler()

    def test_handler(self):
        norm = SampleNorms.get_sample_obligation('test_id')
        pattern_class = CondTEvent()
        pattern_class.event = VariableEvent('evt_test')
        handle_obj = HandleObject(norm)

        result = self.sut.handle(pattern_class, handle_obj)
        
        new_norm: Obligation = result[0]
        self.assertEqual(len(result), 1)

        exp_norm = Obligation(
            'test_id',
            PropMaker.make(
                PredicateFunctionHappens(VariableEvent('evt_test'))
            ),
            'debtor',
            'creditor',
            PropMaker.make_default(),
            PropMaker.make(
                PredicateFunctionHappens(VariableEvent('evt_action'))
            )
        )
        self.assertEqual(new_norm, exp_norm)

if __name__ == '__main__':
    unittest.main()