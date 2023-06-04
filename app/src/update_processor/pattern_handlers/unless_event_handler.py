import copy
from app.classes.patterns.unless_event import UnlessEvent
from app.classes.spec.norm import Norm, Power, Obligation, SurvivingObligation
from app.classes.spec.sym_interval import Interval, SituationExpression
from app.classes.spec.sym_situation import ObligationState, ObligationStateName
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionHappensWithin
from app.classes.spec.p_atoms import PAtomPredicateFalseLiteral
from app.classes.spec.power_function import PFObligation, PFObligationName
from app.classes.helpers.prop_maker import PropMaker
from app.src.update_processor.pattern_handlers.pattern_handler import HandleObject, IHandlePatterns

# This will be a complex one... Will have multiple cases for how this is handled
class UnlessEventHandler(IHandlePatterns):
    def handle(self, pattern: UnlessEvent, handle_object: HandleObject):
        norm: Norm = handle_object.norm
        evt = pattern.event.to_sym_event()

        # If the init_norm is a power to suspend => Then create a new norm with power to resume
        suspension_norm_id = self._get_suspension_norm_id(norm)
        if suspension_norm_id:
            interval = SituationExpression(
                situation = ObligationState(ObligationStateName.Suspension, suspension_norm_id)
            )
            trigger_pred = PredicateFunctionHappensWithin(evt, interval)

            new_power = Power(
                f'pow_resume_{suspension_norm_id}',
                trigger_pred,
                norm.creditor,
                norm.debtor,
                PropMaker.make_default(),
                PFObligation(PFObligationName.Resumed, suspension_norm_id)
            )

            return [new_power]

        # If init norm is a 'not' obligation => create power to suspend it
        not_ob_id = self._get_not_ob(norm)
        if not_ob_id:
            # Check trigger. If false => replace trigger 
            if self._trigger_is_false(norm):
                new_trigger = PredicateFunctionHappens(evt)
                new_norm = copy.deepcopy(norm)
                new_norm.update('trigger', new_trigger)
                
                return [new_norm]

            else:
                # If trigger is Not false => power to suspend
                trigger_pred = PredicateFunctionHappens(evt)
                new_power = Power(
                    f'pow_suspend_{not_ob_id}',
                    trigger_pred,
                    norm.creditor,
                    norm.debtor,
                    PropMaker.make_default(),
                    PFObligation(PFObligationName.Suspended, not_ob_id)
                )

                return [new_power]
        

    def _trigger_is_false(self, norm: Norm):
        trigger_atom = norm.get_component('trigger')
        return isinstance(trigger_atom, PAtomPredicateFalseLiteral)
    
    def _get_not_ob(self, norm: Norm):
        if isinstance(norm, (Obligation, SurvivingObligation)):
            if norm.get_negation('consequent'):
                return norm.id
        
        return None

    def _get_suspension_norm_id(self, norm: Norm):
        if isinstance(norm, Power):
            if isinstance(norm.consequent, PFObligation):
                norm_id = norm.consequent.norm
                return norm_id
        
        return None