from typing import List
import copy
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.operations.user_input import UserInput
from app.classes.spec.point_function import TimeUnit
from app.classes.pattern_classes.pattern_class import PatternClass, EventPatternClass
from app.classes.pattern_classes.within_timespan_event import WithinTimespanEvent
from app.src.pattern_builder.pattern_unit_fillers.pattern_unit_filler import IFillPatternUnit

class TimespanUnitFiller(IFillPatternUnit):
    def fill(self, pattern_class: EventPatternClass, contract:SymboleoContract, input_list: List[UserInput], i: int) -> PatternClass:
        if isinstance(pattern_class, (WithinTimespanEvent)):
            result = copy.deepcopy(pattern_class)
            timespan_unit = input_list[i].value
            result.timespan_unit = TimeUnit[timespan_unit.capitalize()]
            return result
        else:
            return pattern_class
        