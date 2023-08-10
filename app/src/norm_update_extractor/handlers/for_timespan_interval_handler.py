import copy
from typing import List

from app.classes.pattern_classes.pattern_variables import PatternVariable as PV
from app.classes.pattern_classes.for_timespan_interval import ForTimespanInterval
from app.classes.spec.sym_event import VariableEvent, ContractEvent, ContractEventName
from app.classes.spec.norm import Norm
from app.classes.spec.sym_interval import Interval, IntervalFunction
from app.classes.spec.norm_config import NormConfig
from app.classes.spec.predicate_function import PredicateFunctionHappensWithin
from app.classes.spec.sym_point import Point, PointVDE
from app.classes.spec.point_function import PointFunction, TimeUnit

from app.src.object_mappers.timepoint_mapper import IMapTimepoint

from app.src.norm_update_extractor.handlers.norm_update_handler import IHandleNormUpdates

class ForTimespanIntervalHandler(IHandleNormUpdates):
    def __init__(self, timepoint_mapper: IMapTimepoint):
        self.__timepoint_mapper = timepoint_mapper

    def handle(self, pattern_class: ForTimespanInterval, norm_config: NormConfig) -> List[Norm]:
        norm: Norm = norm_config.norm
        component_str = norm_config.parm_config.norm_component
        init_event = norm.get_default_event(component_str)

        evt = pattern_class.event
        timepoint = self.__timepoint_mapper.map(evt)

        timespan_str:str = pattern_class.val_dict[PV.TIMESPAN]
        tv, tu = timespan_str.split(' ')

        tp1 = PointVDE(timepoint) 
        tp2  = PointFunction(
            PointVDE(timepoint), 
            tv, 
            TimeUnit[tu.capitalize()])
        new_interval = Interval(IntervalFunction(tp1, tp2))

        updated_predicate = PredicateFunctionHappensWithin(init_event, new_interval)
        new_norm = copy.deepcopy(norm)
        new_norm.update(component_str, updated_predicate)
        
        return [new_norm]