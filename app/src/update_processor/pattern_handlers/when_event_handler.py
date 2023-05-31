import copy
from app.classes.patterns.when_event import WhenEvent
from app.classes.spec.norm import Norm
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.src.update_processor.pattern_handlers.handle_object import HandleObject
from app.src.update_processor.pattern_handlers.pattern_handler import IHandlePatterns


class WhenEventHandler(IHandlePatterns):
    def handle(self, pattern: WhenEvent, handle_object: HandleObject):
        norm: Norm = handle_object.norm

        evt = pattern.event.to_sym_event()
        new_trigger = PredicateFunctionHappens(evt)
        new_norm = copy.deepcopy(norm)
        new_norm.update('trigger', new_trigger)

        return [new_norm]