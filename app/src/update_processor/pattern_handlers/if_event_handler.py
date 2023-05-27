import copy
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.src.update_processor.pattern_handlers.handle_object import HandleObject
from app.src.update_processor.pattern_handlers.pattern_handler import IHandlePatterns

from app.classes.patterns.if_event import IfEvent

class IfEventHandler(IHandlePatterns):
    def handle(self, pattern: IfEvent, handle_object: HandleObject):
        evt = pattern.event.to_sym_event()
        predicate = PredicateFunctionHappens(evt)
        new_norm = copy.deepcopy(handle_object.norm)
        new_norm.update('antecedent', predicate)
        return [new_norm]
