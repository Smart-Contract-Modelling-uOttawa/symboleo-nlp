import copy

from app.classes.pattern_classes.pattern_variables import PatternVariable as PV
from app.classes.pattern_classes.within_timespan_event import WithinTimespanEvent
from app.classes.spec.norm import Norm
from app.classes.spec.norm_config import NormConfig
from app.classes.spec.predicate_function import PredicateFunctionWHappensBefore
from app.classes.spec.sym_point import Point
from app.classes.spec.point_function import PointFunction, TimeUnit

from app.src.norm_update_extractor.handlers.norm_update_handler import IHandleNormUpdates
from app.src.object_mappers.timespan_mapper import IMapTimespan

class WithinTimespanHandler(IHandleNormUpdates):
    def __init__(self, timespan_mapper: IMapTimespan):
        self.__timespan_mapper = timespan_mapper

    def handle(self, pattern_class: WithinTimespanEvent, norm_config: NormConfig):
        norm: Norm = norm_config.norm
        component_str = norm_config.parm_config.norm_component
        evt = pattern_class.event
        init_event = norm.get_default_event(component_str) 
        
        tv, tu = self.__timespan_mapper.map(pattern_class)
        point_func = Point(PointFunction(evt, tv, tu))
        
        updated_predicate = PredicateFunctionWHappensBefore(init_event, point_func)
        new_norm = copy.deepcopy(norm)
        new_norm.update(component_str, updated_predicate)
        
        return [new_norm]