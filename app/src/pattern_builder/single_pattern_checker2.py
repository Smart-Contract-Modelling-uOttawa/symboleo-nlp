from typing import List, Type
from app.classes.pattern_classes.pattern_variables import PatternVariable
from app.classes.grammar.pattern_values import *
from app.classes.units.all_units import UnitType
from app.classes.operations.user_input import UserInput
from app.classes.pattern_classes.pattern_class import PatternClass

from app.src.pattern_builder.recursive_pattern_checker import ICheckRecursivePattern

class ICheckSinglePattern:
    def check(self, set_to_check: List[UserInput], pc_type: Type[PatternClass]) -> PatternClass:
        raise NotImplementedError()


class SinglePatternChecker2(ICheckSinglePattern):
    def __init__(self, recursive_checker: ICheckRecursivePattern):
        self.__recursive_checker = recursive_checker

    def check(self, set_to_check: List[UserInput], pc_type: Type[PatternClass]) -> PatternClass:
        pv_seq = pc_type.sequence

        if len(set_to_check) < len(pv_seq):
            return False
        
        input_types = [x.unit_type for x in set_to_check]
        
        unit_ind = 0

        my_dict = {}

        # Iterate through the target_set checking the pattern variables
        ## If something doesn't match up, then return false
        for pattern_variable in pv_seq:
            pattern_obj = full_grammar[pattern_variable]
            check, next_ind = self.__recursive_checker.check(input_types, unit_ind, pattern_obj)

            if not check:
                return None
            
            else:
                next_text = [x.value for x in set_to_check[unit_ind:next_ind] if x.value]
                unit_ind = next_ind
                my_dict[pattern_variable] = next_text

        return pc_type(my_dict)

