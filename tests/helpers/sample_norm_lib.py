from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.norm import Norm, Obligation
from app.classes.spec.prop_maker import PropMaker

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
            PropMaker.make_default(),
            'seller',
            'buyer',
            PropMaker.make_default(),
            PropMaker.make(PredicateFunctionHappens(VariableEvent('action')),negation)
       )