import unittest
from unittest.mock import MagicMock

from app.classes.pattern_classes.pattern_variables import PatternVariable as PV
from app.classes.spec.sym_event import VariableEvent
from app.classes.pattern_classes.after_event import AfterEvent
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionWHappensBeforeEvent
from app.classes.helpers.prop_maker import PropMaker
from app.classes.spec.norm import Obligation
from app.classes.spec.norm_config import NormConfig, ParameterConfig

from app.src.norm_update_extractor.handlers.after_event_handler import AfterEventHandler
from tests.helpers.sample_norm_lib import SampleNorms

class AfterEventHandlerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = AfterEventHandler()

    def test_handler(self):
        norm = SampleNorms.get_sample_norm_with_ant('test_id')
        norm_config = NormConfig(norm, ParameterConfig('obligations', 'test_id', 'antecedent'))
        pattern_class = AfterEvent()
        pattern_class.event = VariableEvent('evt_test')

        result = self.sut.handle(pattern_class, norm_config)
        
        new_norm: Obligation = result[0]
        self.assertEqual(len(result), 1)

        exp_norm = Obligation(
            'test_id',
            None,
            'seller',
            'buyer',
            PropMaker.make(
                PredicateFunctionWHappensBeforeEvent(
                    VariableEvent('evt_test'),
                    VariableEvent('ant_action')
                )
            ),
            PropMaker.make(
                PredicateFunctionHappens(
                    VariableEvent('action')
                )
            )
        )

        self.assertEqual(new_norm, exp_norm)

if __name__ == '__main__':
    unittest.main()