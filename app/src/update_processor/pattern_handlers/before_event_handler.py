import copy
from app.classes.frames.before_event_frame import BeforeEventFrame
from app.classes.spec.norm import Norm
from app.classes.spec.predicate_function import PredicateFunctionWHappensBeforeEvent
from app.src.update_processor.pattern_handlers.handle_object import HandleObject
from app.src.update_processor.pattern_handlers.pattern_handler import IHandlePatterns


class BeforeEventHandler(IHandlePatterns):
    def handle(self, frame:BeforeEventFrame, handle_object: HandleObject):
        norm: Norm = handle_object.norm

        evt = frame.event.to_sym_event()
        init_event = norm.get_default_event('consequent') # Need to get consequent?
        updated_predicate = PredicateFunctionWHappensBeforeEvent(init_event, evt)
        new_norm = copy.deepcopy(norm)
        new_norm.update('consequent', updated_predicate)

        return [new_norm]