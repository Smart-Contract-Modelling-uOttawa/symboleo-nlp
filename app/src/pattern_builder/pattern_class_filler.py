from typing import List, Dict
import copy
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.operations.user_input import UnitType, UserInput
from app.classes.pattern_classes.pattern_class import PatternClass
from app.src.pattern_builder.pattern_unit_fillers.pattern_unit_filler import IFillPatternUnit

class IFillPatternClass:
    def fill(self, pattern_class: PatternClass, contract: SymboleoContract, input_list: List[UserInput]) -> PatternClass:
        raise NotImplementedError()

class PatternClassFiller(IFillPatternClass):
    def __init__(
        self, 
        pattern_filler_dict: Dict[UnitType, IFillPatternUnit]
    ):
        self.__pattern_filler_dict = pattern_filler_dict


    def fill(self, pattern_class: PatternClass, contract:SymboleoContract, input_list: List[UserInput]) -> PatternClass:
        
        result = copy.deepcopy(pattern_class)

        # iterate through each of the patterns, and fill the required pieces
        for i, user_input in enumerate(input_list):
            next_pattern_filler = self.__pattern_filler_dict[user_input.unit_type]
            result = next_pattern_filler.fill(result, contract, input_list, i)
        
        return result

