from typing import List
import copy
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.operations.user_input import UserInput
from app.classes.pattern_classes.pattern_class import PatternClass

class IFillPatternUnit:
    def fill(self, pattern_class: PatternClass, contract: SymboleoContract, input_list: List[UserInput], i: int) -> PatternClass:
        raise NotImplementedError()


class DefaultPatternFiller(IFillPatternUnit):
    def fill(self, pattern_class: PatternClass, contract: SymboleoContract, input_list: List[UserInput], i: int) -> PatternClass:
        result = copy.deepcopy(pattern_class)
        # May have some default functionality to fill in the other values
        return result
