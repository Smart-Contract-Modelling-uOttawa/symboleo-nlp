from typing import List
import copy
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.operations.user_input import UserInput
from app.classes.pattern_classes.pattern_class import PatternClass
from app.classes.pattern_classes.before_date import BeforeDate
from app.src.pattern_builder.pattern_unit_fillers.pattern_unit_filler import IFillPatternUnit

class DateFiller(IFillPatternUnit):
    def fill(self, pattern_class: PatternClass, contract: SymboleoContract, input_list: List[UserInput], i: int) -> PatternClass:
        if isinstance(pattern_class, (BeforeDate)):
            result = copy.deepcopy(pattern_class)
            result.date_text = input_list[i].value
            return result
        else:
            return pattern_class
        