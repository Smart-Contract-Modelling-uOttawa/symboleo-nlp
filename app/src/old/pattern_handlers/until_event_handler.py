import copy
from app.classes.patterns.until_event import UntilEvent
from app.classes.spec.norm import Norm
from app.classes.spec.predicate_function import PredicateFunctionWHappensBeforeEvent
from app.classes.operations.handle_object import HandleObject
from app.src.update_processor.pattern_handlers.pattern_handler import IHandlePatterns


class UntilEventHandler(IHandlePatterns):
    def handle(self, pattern: UntilEvent, handle_object: HandleObject):
        norm: Norm = handle_object.norm

        evt = pattern.event.to_sym_event()
        init_event = norm.get_default_event('consequent') # Need to get consequent?
        updated_predicate = PredicateFunctionWHappensBeforeEvent(init_event, evt)
        new_norm = copy.deepcopy(norm)
        new_norm.update('consequent', updated_predicate)

        return [new_norm]