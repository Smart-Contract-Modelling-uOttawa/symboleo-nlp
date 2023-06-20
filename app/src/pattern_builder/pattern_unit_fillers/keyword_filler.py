from typing import List
import copy
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.operations.user_input import UserInput
from app.classes.patterns.pattern_classes import *
from app.src.pattern_builder.pattern_unit_fillers.pattern_unit_filler import IFillPatternUnit

class KeywordFiller(IFillPatternUnit):
    def __init__(self, keyword:str):
        self.__keyword = keyword

    def fill(self, pattern_class: PatternClass, contract: SymboleoContract, input_list: List[UserInput], i: int) -> PatternClass:
        result = copy.deepcopy(pattern_class)
        result.keyword = self.__keyword
        return result


        