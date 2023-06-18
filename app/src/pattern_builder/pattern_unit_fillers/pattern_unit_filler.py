from typing import List
import copy
from app.classes.patterns.pattern_classes import *
from app.classes.operations.user_input import UserInput
from app.classes.patterns.pattern_classes import List, PatternClass

# TODO: This will take a bigger role (again)
## It will also be responsible for updating the nl information
## Will require the contract as input as well
## Might need these for all the units then as well...
class IFillPatternUnit:
    def fill(self, pattern_class: PatternClass, input_list: List[UserInput], i: int) -> PatternClass:
        raise NotImplementedError()


class DefaultPatternFiller(IFillPatternUnit):
    def fill(self, pattern_class: PatternClass, input_list: List[UserInput], i: int) -> PatternClass:
        result = copy.deepcopy(pattern_class)
        return result
