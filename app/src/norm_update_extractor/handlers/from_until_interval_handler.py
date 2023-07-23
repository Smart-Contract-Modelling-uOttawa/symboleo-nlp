import copy
from typing import List

from app.classes.pattern_classes.from_until_interval import FromUntilInterval
from app.classes.spec.norm import Norm
from app.classes.spec.sym_interval import Interval, IntervalFunction
from app.classes.spec.norm_config import NormConfig
from app.classes.spec.predicate_function import PredicateFunctionHappensWithin
from app.classes.spec.sym_point import Point, PointVDE

from app.src.norm_update_extractor.handlers.norm_update_handler import IHandleNormUpdates

class FromUntilIntervalHandler(IHandleNormUpdates):
    def handle(self, pattern_class: FromUntilInterval, norm_config: NormConfig) -> List[Norm]:
        norm: Norm = norm_config.norm
        component_str = norm_config.parm_config.norm_component
        init_event = norm.get_default_event(component_str)

        tp1 = PointVDE(pattern_class.timepoint1)
        tp2 = PointVDE(pattern_class.timepoint2)
        new_interval = Interval(IntervalFunction(tp1, tp2))

        updated_predicate = PredicateFunctionHappensWithin(init_event, new_interval)
        new_norm = copy.deepcopy(norm)
        new_norm.update(component_str, updated_predicate)
        
        return [new_norm]