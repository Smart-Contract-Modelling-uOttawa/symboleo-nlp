from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.power_function import PFObligation, PFObligationName
from app.classes.spec.norm import Norm, Obligation, Power
from app.classes.helpers.prop_maker import PropMaker

class SampleNorms:
    @staticmethod
    def get_sample_norm(id='test_id') -> Norm:
        return Obligation(
            id,
            None,
            'seller',
            'buyer',
            PropMaker.make_default(),
            PropMaker.make(PredicateFunctionHappens(VariableEvent('action')))
       )
    
    @staticmethod
    def get_sample_obligation(id='test_id', negation=False) -> Norm:
        return Obligation(
            id,
            None,
            'debtor',
            'creditor',
            PropMaker.make_default(),
            PropMaker.make(PredicateFunctionHappens(VariableEvent('evt_action')), negation)
       )
    
    @staticmethod
    def get_suspension_power(id='test_pow', ob_id='ob_test') -> Norm:
        return Power(
            id,
            None,
            'debtor',
            'creditor',
            PropMaker.make_default(),
            PFObligation(PFObligationName.Suspended, ob_id)
        )