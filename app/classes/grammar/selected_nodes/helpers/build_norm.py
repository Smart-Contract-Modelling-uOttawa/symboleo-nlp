from app.classes.spec.contract_spec import Norm, Power
from app.classes.spec.power_function import PFObligation, PFObligationName
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.spec.sym_event import SymEvent
from app.classes.spec.prop_maker import PropMaker

# TODO: This should be in src somewhere... 
## Will likely have more like this
## But actually, maybe all selectedNodes need to go there...
class NormBuilder:
    @staticmethod
    def build(norm1: Norm, event: SymEvent):
        return Power(
            f'pow_suspend_{norm1.id}', 
            PropMaker.make(PredicateFunctionHappens(event)), 
            norm1.creditor, 
            norm1.debtor, 
            PropMaker.make_default(), 
            PFObligation(PFObligationName.Suspended, norm1.id)
        )
    