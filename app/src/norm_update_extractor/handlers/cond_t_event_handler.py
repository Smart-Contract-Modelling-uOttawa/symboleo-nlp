import copy
from app.classes.spec.norm_config import NormConfig
from app.classes.pattern_classes.cond_t_event import CondTEvent
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.src.norm_update_extractor.handlers.norm_update_handler import IHandleNormUpdates


class CondTEventHandler(IHandleNormUpdates):
    def handle(self, pattern_class: CondTEvent, norm_config: NormConfig):
        evt = pattern_class.event
        predicate = PredicateFunctionHappens(evt)
        new_norm = copy.deepcopy(norm_config.norm)
        new_norm.update('trigger', predicate)

        return [new_norm]