from app.classes.spec.helpers import VariableDotExpression
from app.classes.spec.p_atoms import PAtomPredicate
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.symboleo_spec import Norm, Obligation, PAnd, PComparison, PEquality, Proposition



class SampleNorms:
    @staticmethod
    def get_sample_norm() -> Norm:
        return Obligation(
            'test_id',
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