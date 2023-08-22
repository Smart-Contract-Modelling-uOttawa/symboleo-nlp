from typing import List
from app.classes.pattern_classes.pattern_variables import PatternVariable
from app.classes.grammar.full_grammar import *
from app.classes.units.all_units import UnitType

from app.src.pattern_builder.recursive_pattern_checker import ICheckRecursivePattern

class ICheckSinglePattern:
    def check(self, set_to_check: List[UnitType], target_set: List[PatternVariable]) -> bool:
        raise NotImplementedError()
    
class SinglePatternChecker(ICheckSinglePattern):
    def __init__(self, recursive_checker: ICheckRecursivePattern):
        self.__recursive_checker = recursive_checker

    def check(self, set_to_check: List[UnitType], target_set: List[PatternVariable]) -> bool:
        if len(set_to_check) < len(target_set):
            return False
        
        unit_ind = 0

        # Iterate through the target_set checking the pattern variables
        ## If something doesn't match up, then return false
        for pattern_variable in target_set:
            pattern_obj = FULL_GRAMMAR[pattern_variable]
            check, unit_ind = self.__recursive_checker.check(set_to_check, unit_ind, pattern_obj)

            if not check:
                return False

        return True

