from app.classes.spec.norm import Norm, Power
from app.classes.spec.power_function import PFObligation, PFObligationName
from app.classes.spec.predicate_function import PredicateFunction, PredicateFunctionHappens
from app.classes.spec.sym_event import SymEvent
from app.classes.spec.prop_maker import PropMaker

# TODO: This should be in src somewhere... 
## Will likely have more like this
## But actually, maybe all selectedNodes need to go there...
class NormBuilder:
    @staticmethod
    def build(norm1: Norm, event: SymEvent):
        # Need to do some checks in here...
        ## If the initial norm involves a suspension, then we need to make a 'Resume'

        x = NormBuilder.get_suspension_info(norm1)
        if x:
            pow_name = f'pow_resume_{x}'
            new_cons = PFObligation(PFObligationName.Resumed, x)
        else:
            new_cons = PFObligation(PFObligationName.Suspended, norm1.id)
            pow_name = f'pow_suspend_{norm1.id}'

        return Power(
            pow_name, 
            PropMaker.make(PredicateFunctionHappens(event)), 
            norm1.creditor, 
            norm1.debtor, 
            PropMaker.make_default(), 
            new_cons
        )
    
    @staticmethod
    def get_suspension_info(norm: Norm):
        cons = norm.consequent
        if type(cons) == PFObligation:
            if cons.name == PFObligationName.Suspended:
                return cons.norm

        return False

    