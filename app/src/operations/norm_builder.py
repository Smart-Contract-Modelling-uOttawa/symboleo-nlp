from app.classes.spec.norm import Norm, Power
from app.classes.spec.power_function import PFObligation, PFObligationName
from app.classes.spec.predicate_function import PredicateFunction, PredicateFunctionHappens
from app.classes.spec.sym_event import SymEvent
from app.classes.helpers.prop_maker import PropMaker

# May be better to rename to suspensive norm builder or something like that
class IBuildNorms:
    def build(self, norm1: Norm, event: SymEvent) -> Norm:
        raise NotImplementedError()

# TODO: E2 - Re-integrate this... into UnlessEvent PatternHandler
class NormBuilder(IBuildNorms):
    def build(self, norm1: Norm, event: SymEvent) -> Norm:
        # Need to do some checks in here...
        ## If the initial norm involves a suspension, then we need to make a 'Resume'
        x = self._get_suspension_info(norm1)
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
    
    
    def _get_suspension_info(self, norm: Norm):
        cons = norm.consequent
        if type(cons) == PFObligation:
            if cons.name == PFObligationName.Suspended:
                return cons.norm

        return False

    