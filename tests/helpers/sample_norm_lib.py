from app.classes.spec.helpers import VariableDotExpression
from app.classes.spec.p_atoms import PAtomPredicate
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.proposition import PAnd, PComparison, PEquality, Proposition
from app.classes.spec.contract_spec import Norm, Obligation


class SampleNorms:
    @staticmethod
    def get_sample_norm(id='test_id') -> Norm:
        return Obligation(
            id,
            None,
            VariableDotExpression('seller'),
            VariableDotExpression('buyer'),
            None,
            Proposition([PAnd([PEquality([PComparison([
                PAtomPredicate(
                    PredicateFunctionHappens(
                        VariableEvent(
                            VariableDotExpression('action')
                        )
                    )
                )
            ])])])])
       )
    
    @staticmethod
    def get_sample_obligation(id='test_id') -> Norm:
        return Obligation(
            id,
            None,
            VariableDotExpression('seller'),
            VariableDotExpression('buyer'),
            None,
            Proposition([PAnd([PEquality([PComparison([
                PAtomPredicate(
                    PredicateFunctionHappens(
                        VariableEvent(
                            VariableDotExpression('action')
                        )
                    )
                )
            ])])])])
       )