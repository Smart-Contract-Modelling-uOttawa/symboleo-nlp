import copy
from typing import List

from app.classes.pattern_classes.pattern_variables import PatternVariable as PV
from app.classes.pattern_classes.between_interval import BetweenInterval
from app.classes.spec.norm import Norm
from app.classes.spec.sym_interval import Interval, IntervalFunction
from app.classes.spec.norm_config import NormConfig
from app.classes.spec.predicate_function import PredicateFunctionHappensWithin
from app.classes.spec.sym_point import Point, PointVDE

from app.src.norm_update_extractor.handlers.norm_update_handler import IHandleNormUpdates
from app.src.object_mappers.date_mapper import IMapDate

class BetweenIntervalHandler(IHandleNormUpdates):
    def __init__(self, date_mapper: IMapDate):
        self.__date_mapper = date_mapper

    def handle(self, pattern_class: BetweenInterval, norm_config: NormConfig) -> List[Norm]:
        norm: Norm = norm_config.norm
        component_str = norm_config.parm_config.norm_component
        init_event = norm.get_default_event(component_str)

        d1 = self.__date_mapper.map(pattern_class.val_dict[PV.DATE], PV.DATE, norm_config)
        d2 = self.__date_mapper.map(pattern_class.val_dict[PV.DATE2], PV.DATE2, norm_config)
        tp1 = PointVDE(d1)
        tp2 = PointVDE(d2)
        new_interval = Interval(IntervalFunction(tp1, tp2))

        updated_predicate = PredicateFunctionHappensWithin(init_event, new_interval)
        new_norm = copy.deepcopy(norm)
        new_norm.update(component_str, updated_predicate)
        
        return [new_norm]