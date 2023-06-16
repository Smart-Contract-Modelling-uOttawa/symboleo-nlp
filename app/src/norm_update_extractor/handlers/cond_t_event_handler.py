import copy
from app.classes.patterns.pattern_classes import CondTEvent
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.operations.handle_object import HandleObject
from app.src.norm_update_extractor.handlers.norm_update_handler import IHandleNormUpdates


class CondTEventHandler(IHandleNormUpdates):
    def handle(self, pattern_class: CondTEvent, handle_object: HandleObject):
        evt = pattern_class.event
        predicate = PredicateFunctionHappens(evt)
        new_norm = copy.deepcopy(handle_object.norm)
        new_norm.update('trigger', predicate)

        return [new_norm]