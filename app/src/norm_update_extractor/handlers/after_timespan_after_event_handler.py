import copy
from app.classes.pattern_classes.after_timespan_after_event import AfterTimespanAfterEvent
from app.classes.spec.norm import Norm
from app.classes.spec.norm_config import NormConfig
from app.classes.spec.predicate_function import PredicateFunctionHappensAfter
from app.classes.spec.sym_point import Point
from app.classes.spec.point_function import PointFunction
from app.src.norm_update_extractor.handlers.norm_update_handler import IHandleNormUpdates


class AfterTimespanAfterEventHandler(IHandleNormUpdates):
    def handle(self, pattern_class: AfterTimespanAfterEvent, norm_config: NormConfig):
        norm: Norm = norm_config.norm
        component_str = norm_config.parm_config.norm_component
        
        evt = pattern_class.event
        init_event = norm.get_default_event('consequent') 
        point_func = Point(PointFunction(evt, pattern_class.timespan_value, pattern_class.timespan_unit))
        updated_predicate = PredicateFunctionHappensAfter(init_event, point_func)
        new_norm = copy.deepcopy(norm)
        new_norm.update('consequent', updated_predicate)
        
        return [new_norm]