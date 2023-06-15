from typing import List
import copy
from app.classes.patterns.pattern_classes import *
from app.classes.operations.user_input import UserInput
from app.classes.patterns.pattern_classes import List, PatternClass

class IFillPatternUnit:
    def fill(self, pattern_class: PatternClass, input_list: List[UserInput], i: int) -> PatternClass:
        raise NotImplementedError()


class DefaultPatternFiller(IFillPatternUnit):
    def fill(self, pattern_class: PatternClass, input_list: List[UserInput], i: int) -> PatternClass:
        result = copy.deepcopy(pattern_class)
        return result
