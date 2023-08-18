import copy
from typing import List

from app.classes.pattern_classes.pattern_variables import PatternVariable as PV
from app.classes.pattern_classes.before_date import BeforeDate
from app.classes.spec.norm import Norm
from app.classes.spec.norm_config import NormConfig
from app.classes.spec.predicate_function import PredicateFunctionSHappensBefore
from app.classes.spec.sym_point import Point, PointVDE

from app.src.norm_update_extractor.handlers.norm_update_handler import IHandleNormUpdates
from app.src.object_mappers.date_mapper import IMapDate

class BeforeDateHandler(IHandleNormUpdates):
    def __init__(self, date_mapper: IMapDate):
        self.__date_mapper = date_mapper

    def handle(self, pattern_class: BeforeDate, norm_config: NormConfig) -> List[Norm]:
        norm: Norm = norm_config.norm
        component_str = norm_config.parm_config.norm_component
        init_event = norm.get_default_event(component_str)
        
        date_text = self.__date_mapper.map(pattern_class.val_dict[PV.DATE], PV.DATE, norm_config)
        point_val = Point(PointVDE(date_text))
        
        updated_predicate = PredicateFunctionSHappensBefore(init_event, point_val)
        new_norm = copy.deepcopy(norm)
        new_norm.update(component_str, updated_predicate)
        
        return [new_norm]