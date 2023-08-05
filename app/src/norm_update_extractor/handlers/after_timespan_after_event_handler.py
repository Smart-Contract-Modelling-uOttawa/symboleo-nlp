import copy

from app.classes.pattern_classes.pattern_variables import PatternVariable as PV
from app.classes.pattern_classes.after_timespan_after_event import AfterTimespanAfterEvent
from app.classes.spec.norm import Norm
from app.classes.spec.norm_config import NormConfig
from app.classes.spec.predicate_function import PredicateFunctionHappensAfter
from app.classes.spec.sym_point import Point
from app.classes.spec.point_function import PointFunction, TimeUnit
from app.src.norm_update_extractor.handlers.norm_update_handler import IHandleNormUpdates


class AfterTimespanAfterEventHandler(IHandleNormUpdates):
    def handle(self, pattern_class: AfterTimespanAfterEvent, norm_config: NormConfig):
        norm: Norm = norm_config.norm
        
        evt = pattern_class.event
        init_event = norm.get_default_event('consequent')
        
        timespan_str:str = pattern_class.val_dict[PV.TIMESPAN]
        tv, tu = timespan_str.split(' ')
        point_func = Point(PointFunction(evt, tv, TimeUnit[tu.capitalize()]))
        
        updated_predicate = PredicateFunctionHappensAfter(init_event, point_func)
        new_norm = copy.deepcopy(norm)
        new_norm.update('consequent', updated_predicate)
        
        return [new_norm]