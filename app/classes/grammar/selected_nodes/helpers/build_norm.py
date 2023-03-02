from app.classes.spec.contract_spec import Norm, Power
from app.classes.spec.power_function import PFObligation
from app.classes.spec.proposition import Proposition, PAnd, PEquality, PComparison, PNegAtom, PAtom
from app.classes.spec.p_atoms import PAtomPredicate
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.spec.sym_event import SymEvent

# TODO: This should be in src somewhere... 
## Will likely have more like this
## But actually, maybe all selectedNodes need to go there...
class NormBuilder:
    @staticmethod
    def build(norm1: Norm, event: SymEvent):
        pf = PFObligation('Suspended', norm1.id)
        trigger = Proposition([PAnd([PEquality([PComparison([PNegAtom(PAtomPredicate(
            PredicateFunctionHappens(event)
        ))])])])])
        norm = Power(f'pow_suspend_{norm1.id}', trigger, norm1.creditor, norm1.debtor, None, pf)
        return norm