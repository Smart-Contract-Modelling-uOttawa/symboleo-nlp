import copy
from typing import List

from app.classes.pattern_classes.pattern_variables import PatternVariable as PV
from app.classes.pattern_classes.after_event import AfterEvent
from app.classes.spec.norm import Norm
from app.classes.spec.norm_config import NormConfig
from app.classes.spec.predicate_function import PredicateFunctionWHappensBeforeEvent

from app.src.norm_update_extractor.handlers.norm_update_handler import IHandleNormUpdates

class AfterEventHandler(IHandleNormUpdates):
    def handle(self, pattern_class: AfterEvent, norm_config: NormConfig) -> List[Norm]:
        norm: Norm = norm_config.norm
        component_str = norm_config.parm_config.norm_component
        init_event = norm.get_default_event(component_str)
        
        new_event = pattern_class.event
        
        updated_predicate = PredicateFunctionWHappensBeforeEvent(new_event, init_event) # Swapped event order
        new_norm = copy.deepcopy(norm)
        new_norm.update(component_str, updated_predicate)
        
        return [new_norm]