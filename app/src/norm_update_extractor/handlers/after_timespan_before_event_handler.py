import copy

from app.classes.pattern_classes.pattern_variables import PatternVariable as PV
from app.classes.pattern_classes.after_timespan_before_event import AfterTimespanBeforeEvent
from app.classes.spec.norm import Norm
from app.classes.spec.norm_config import NormConfig
from app.classes.spec.predicate_function import PredicateFunctionHappensAfter
from app.classes.spec.sym_point import Point
from app.classes.spec.point_function import PointFunction, TimeUnit
from app.src.norm_update_extractor.handlers.norm_update_handler import IHandleNormUpdates
from app.src.object_mappers.timespan_mapper import IMapTimespan


class AfterTimespanBeforeEventHandler(IHandleNormUpdates):
    def __init__(self, timespan_mapper: IMapTimespan):
        self.__timespan_mapper = timespan_mapper

    def handle(self, pattern_class: AfterTimespanBeforeEvent, norm_config: NormConfig):
        norm: Norm = norm_config.norm
        component_str = norm_config.parm_config.norm_component
        evt = pattern_class.event
        init_event = norm.get_default_event(component_str)

        tv, tu = self.__timespan_mapper.map(pattern_class)
        negated_time_value = str(-1 * int(tv))
        point_func = Point(PointFunction(evt, negated_time_value, tu))
        
        updated_predicate = PredicateFunctionHappensAfter(init_event, point_func)
        new_norm = copy.deepcopy(norm)
        new_norm.update(component_str, updated_predicate)
        
        return [new_norm]