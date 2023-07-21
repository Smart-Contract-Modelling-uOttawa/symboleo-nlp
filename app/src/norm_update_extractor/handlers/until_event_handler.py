import copy
from typing import List

from app.classes.pattern_classes.until_event import UntilEvent
from app.classes.spec.norm import Norm
from app.classes.spec.predicate_function import PredicateFunctionWHappensBefore
from app.classes.spec.sym_point import Point, PointVDE
from app.classes.operations.handle_object import HandleObject

from app.src.norm_update_extractor.handlers.norm_update_handler import IHandleNormUpdates

class UntilEventHandler(IHandleNormUpdates):
    # TODO: This only applies to negated events. Can have a check here
    ## Better to handle earlier though. Prevent it...
    def handle(self, pattern_class: UntilEvent, handle_object: HandleObject) -> List[Norm]:
        norm: Norm = handle_object.norm
        init_event = norm.get_default_event('consequent') # Need to get consequent?
        new_event = pattern_class.event
        updated_predicate = PredicateFunctionWHappensBefore(init_event, new_event)
        new_norm = copy.deepcopy(norm)
        new_norm.update('consequent', updated_predicate)
        
        return [new_norm]