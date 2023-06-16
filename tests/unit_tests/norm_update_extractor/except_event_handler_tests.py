import unittest
from unittest.mock import MagicMock
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.power_function import PFObligation, PFObligationName
from app.classes.spec.sym_interval import SituationExpression
from app.classes.spec.sym_situation import ObligationState, ObligationStateName
from app.classes.patterns.pattern_classes import ExceptEvent
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionHappensWithin
from app.classes.operations.handle_object import HandleObject
from app.classes.helpers.prop_maker import PropMaker
from app.classes.spec.norm import Obligation, Power

from app.src.norm_update_extractor.handlers.except_event_handler import ExceptEventHandler
from tests.helpers.sample_norm_lib import SampleNorms

class ExceptEventHandlerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = ExceptEventHandler()

    # Obligation not to => power to suspend
    def test_handler(self):
        norm = SampleNorms.get_sample_obligation('test_id', negation=True)
        pattern_class = ExceptEvent()
        pattern_class.event = VariableEvent('evt_test')
        handle_obj = HandleObject(norm)

        result = self.sut.handle(pattern_class, handle_obj)

        new_norm: Obligation = result[0]
        self.assertEqual(len(result), 1)

        exp_norm = Power(
            'pow_suspend_test_id',
            PropMaker.make(
                PredicateFunctionHappens(VariableEvent('evt_test'))
            ),
            'creditor',
            'debtor',
            PropMaker.make_default(),
            PFObligation(PFObligationName.Suspended, 'test_id')
        )

        self.assertEqual(new_norm, exp_norm)
    
    # Power to suspend => power to resume
    def test_handler(self):
        norm = SampleNorms.get_suspension_power('test_id', 'ob_test')
        pattern_class = ExceptEvent()
        pattern_class.event = VariableEvent('evt_test')
        handle_obj = HandleObject(norm)

        result = self.sut.handle(pattern_class, handle_obj)

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