import copy
from app.classes.patterns.unless_event import UnlessEvent
from app.classes.spec.norm import Norm, Power
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.spec.power_function import PFObligation, PFObligationName
from app.classes.spec.prop_maker import PropMaker
from app.src.update_processor.pattern_handlers.pattern_handler import HandleObject, IHandlePatterns


class UnlessEventHandler(IHandlePatterns):
    def handle(self, pattern: UnlessEvent, handle_object: HandleObject):
        norm: Norm = handle_object.norm
        evt = pattern.event.to_sym_event()

        # If the init_norm is a power to suspend
        # Then create a new norm with power to resume
        suspension_norm_id = self._get_suspension_norm_id(norm)
        if suspension_norm_id:
            new_power = Power(
                f'pow_resume_{suspension_norm_id}',
                PropMaker.make(PredicateFunctionHappens(evt)),
                norm.creditor,
                norm.debtor,
                PropMaker.make_default(),
                PFObligation(PFObligationName.Resumed, suspension_norm_id)
            )

            return [new_power]
        


    def _get_suspension_norm_id(self, norm: Norm):
        if isinstance(norm, Power):
            if isinstance(norm.consequent, PFObligation):
                norm_id = norm.consequent.norm
                return norm_id
        
        return None