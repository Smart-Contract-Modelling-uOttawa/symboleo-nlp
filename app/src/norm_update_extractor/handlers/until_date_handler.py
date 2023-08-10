import copy
from typing import List

from app.classes.pattern_classes.pattern_variables import PatternVariable as PV
from app.classes.pattern_classes.until_date import UntilDate
from app.classes.spec.norm import Norm
from app.classes.spec.norm_config import NormConfig
from app.classes.spec.predicate_function import PredicateFunctionSHappensBefore
from app.classes.spec.sym_point import Point, PointVDE

from app.src.norm_update_extractor.handlers.norm_update_handler import IHandleNormUpdates

class UntilDateHandler(IHandleNormUpdates):
    def handle(self, pattern_class: UntilDate, norm_config: NormConfig) -> List[Norm]:
        norm: Norm = norm_config.norm
        component_str = norm_config.parm_config.norm_component
        init_event = norm.get_default_event(component_str) 

        if not norm.get_negation(component_str):
            raise ValueError('UntilDateHandler can only be used with a negated norm')

        date_text = pattern_class.val_dict[PV.DATE]
        point_val = Point(PointVDE(f'"{date_text}"'))
        
        updated_predicate = PredicateFunctionSHappensBefore(init_event, point_val)
        new_norm = copy.deepcopy(norm)
        new_norm.update(component_str, updated_predicate)
        
        return [new_norm]