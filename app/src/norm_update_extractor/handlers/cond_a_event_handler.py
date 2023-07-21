import copy

from app.classes.pattern_classes.cond_a_event import CondAEvent
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.operations.handle_object import HandleObject
from app.src.norm_update_extractor.handlers.norm_update_handler import IHandleNormUpdates


class CondAEventHandler(IHandleNormUpdates):
    def handle(self, pattern_class: CondAEvent, handle_object: HandleObject):
        evt = pattern_class.event
        print(evt)
        predicate = PredicateFunctionHappens(evt)
        new_norm = copy.deepcopy(handle_object.norm)
        new_norm.update('antecedent', predicate)

        return [new_norm]