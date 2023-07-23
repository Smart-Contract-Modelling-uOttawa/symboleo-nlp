import unittest
from unittest.mock import MagicMock
from app.classes.spec.sym_event import VariableEvent
from app.classes.pattern_classes.cond_a_event import CondAEvent
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.helpers.prop_maker import PropMaker
from app.classes.spec.norm import Obligation

from app.src.norm_update_extractor.handlers.cond_a_event_handler import CondAEventHandler
from tests.helpers.sample_norm_lib import SampleNorms

class CondAEventHandlerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = CondAEventHandler()

    def test_handler(self):
        norm_config = SampleNorms.get_sample_obligation_config('test_id')
        pattern_class = CondAEvent()
        pattern_class.event = VariableEvent('evt_test')

        result = self.sut.handle(pattern_class, norm_config)

        new_norm: Obligation = result[0]
        self.assertEqual(len(result), 1)

        exp_norm = Obligation(
            'test_id',
            None,
            'debtor',
            'creditor',
            PropMaker.make(
                PredicateFunctionHappens(VariableEvent('evt_test'))
            ),
            PropMaker.make(
                PredicateFunctionHappens(VariableEvent('evt_action'))
            )
        )
        
        self.assertEqual(new_norm, exp_norm)
        

if __name__ == '__main__':
    unittest.main()