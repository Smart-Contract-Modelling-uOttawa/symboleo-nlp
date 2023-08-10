import copy
from typing import List

from app.classes.pattern_classes.pattern_variables import PatternVariable as PV
from app.classes.pattern_classes.during_time_period import DuringTimePeriod
from app.classes.spec.norm import Norm
from app.classes.spec.sym_interval import Interval, IntervalFunction
from app.classes.spec.norm_config import NormConfig
from app.classes.spec.predicate_function import PredicateFunctionHappensWithin
from app.classes.spec.sym_point import Point, PointVDE

from app.src.object_mappers.time_period_mapper import IMapTimePeriod

from app.src.norm_update_extractor.handlers.norm_update_handler import IHandleNormUpdates

class DuringTimePeriodHandler(IHandleNormUpdates):
    def __init__(self, time_period_mapper: IMapTimePeriod):
        self.__time_period_mapper = time_period_mapper


    def handle(self, pattern_class: DuringTimePeriod, norm_config: NormConfig) -> List[Norm]:
        norm: Norm = norm_config.norm
        component_str = norm_config.parm_config.norm_component
        init_event = norm.get_default_event(component_str)

        time_period = self.__time_period_mapper.map(pattern_class)
        tp1 = PointVDE(time_period.start)
        tp2 = PointVDE(time_period.end)
        new_interval = Interval(IntervalFunction(tp1, tp2))

        updated_predicate = PredicateFunctionHappensWithin(init_event, new_interval)
        new_norm = copy.deepcopy(norm)
        new_norm.update(component_str, updated_predicate)
        
        return [new_norm]