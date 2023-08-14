import unittest
from unittest.mock import MagicMock

from app.classes.pattern_classes.pattern_variables import PatternVariable as PV
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.power_function import PFObligation, PFObligationName
from app.classes.spec.sym_interval import SituationExpression
from app.classes.spec.sym_situation import ObligationState, ObligationStateName
from app.classes.pattern_classes.except_event import ExceptEvent
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionHappensWithin
from app.classes.helpers.prop_maker import PropMaker
from app.classes.spec.norm import Obligation, Power
from app.classes.spec.norm_config import NormConfig, ParameterConfig

from app.src.norm_update_extractor.handlers.except_event_handler import ExceptEventHandler
from tests.helpers.sample_norm_lib import SampleNorms

class ExceptEventHandlerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = ExceptEventHandler()

    # Obligation not to => power to suspend
    def test_handler(self):
        norm_config = SampleNorms.get_sample_obligation_config('test_id', negation=True)
        pattern_class = ExceptEvent()
        pattern_class.event = VariableEvent('evt_test')

        result = self.sut.handle(pattern_class, norm_config)

        new_norm: Obligation = result[0]
        self.assertEqual(len(result), 1)

        exp_norm = Power(
            'pow_terminate_test_id',
            PropMaker.make(
                PredicateFunctionHappens(VariableEvent('evt_test'))
            ),
            'creditor',
            'debtor',
            PropMaker.make_default(),
            PFObligation(PFObligationName.Terminated, 'test_id')
        )

        self.assertEqual(new_norm, exp_norm)
    
    # Power to suspend => power to resume
    def test_handler(self):
        norm = SampleNorms.get_suspension_power('test_id', 'ob_test')
        pattern_class = ExceptEvent()
        pattern_class.event = VariableEvent('evt_test')
        norm_config = NormConfig(norm, ParameterConfig('powers', 'test_id', 'trigger'))

        result = self.sut.handle(pattern_class, norm_config)

        new_norm: Obligation = result[0]
        self.assertEqual(len(result), 1)

        exp_norm = Power(
            'pow_resume_ob_test',
            PropMaker.make(
                PredicateFunctionHappensWithin(
                    VariableEvent('evt_test'),
                    SituationExpression(
                        ObligationState(ObligationStateName.Suspension, 'obligations.ob_test')
                    ) 
                )
            ),
            'creditor',
            'debtor',
            PropMaker.make_default(),
            PFObligation(PFObligationName.Resumed, 'ob_test')
        )

        self.assertEqual(new_norm, exp_norm)
        

if __name__ == '__main__':
    unittest.main()