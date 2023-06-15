from typing import List
import copy
from app.classes.operations.user_input import UserInput
from app.classes.patterns.pattern_classes import *
from app.src.update_processor2.pattern_unit_fillers.pattern_unit_filler import IFillPatternUnit

class DateFiller(IFillPatternUnit):
    def fill(self, pattern_class: PatternClass, input_list: List[UserInput], i: int) -> PatternClass:
        if isinstance(pattern_class, (BeforeDate)):
            result = copy.deepcopy(pattern_class)
            result.date_text = input_list[i].value
            return result
        else:
            return pattern_class
        