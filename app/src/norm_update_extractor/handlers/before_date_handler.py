import copy
from typing import List
from app.classes.patterns.pattern_classes import *
from app.classes.spec.norm import Norm
from app.classes.spec.predicate_function import PredicateFunctionSHappensBefore
from app.classes.spec.sym_point import Point, PointVDE
from app.classes.operations.handle_object import HandleObject
from app.src.norm_update_extractor.handlers.norm_update_handler import IHandleNormUpdates


class BeforeDateHandler(IHandleNormUpdates):
    def handle(self, pattern_class: BeforeDate, handle_object: HandleObject) -> List[Norm]:
        norm: Norm = handle_object.norm
        init_event = norm.get_default_event('consequent') # Need to get consequent?
        point_val = Point(PointVDE(f'"{pattern_class.date_text}"'))
        updated_predicate = PredicateFunctionSHappensBefore(init_event, point_val)
        new_norm = copy.deepcopy(norm)
        new_norm.update('consequent', updated_predicate)
        
        return [new_norm]