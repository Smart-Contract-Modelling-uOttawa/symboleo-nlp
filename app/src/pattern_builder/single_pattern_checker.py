from typing import List, Type, Dict
from app.classes.pattern_classes.pattern_variables import PatternVariable
from app.classes.grammar.full_grammar import *
from app.classes.units.all_units import UnitType
from app.classes.operations.user_input import UserInput
from app.classes.pattern_classes.pattern_class import PatternClass

from app.src.pattern_builder.recursive_pattern_checker import ICheckRecursivePattern

class ICheckSinglePattern:
    def check(self, set_to_check: List[UserInput], pc_type: Type[PatternClass]) -> PatternClass:
        raise NotImplementedError()


class SinglePatternChecker(ICheckSinglePattern):
    def __init__(self, recursive_checker: ICheckRecursivePattern):
        self.__recursive_checker = recursive_checker

    def check(self, set_to_check: List[UserInput], pc_type: Type[PatternClass]) -> PatternClass:
        pv_seq = pc_type.sequence

        if len(set_to_check) < len(pv_seq):
            return False
        
        input_types = [x.unit_type for x in set_to_check]
        
        unit_ind = 0

        my_dict: Dict[PatternVariable, List[str]] = {}

        # Iterate through the target_set checking the pattern variables
        ## If something doesn't match up, then return false
        for pattern_variable in pv_seq:
            pattern_obj = FULL_GRAMMAR[pattern_variable]
            check, next_ind = self.__recursive_checker.check(input_types, unit_ind, pattern_obj)

            if not check:
                return None
            else:
                next_arr = [x.value for x in set_to_check[unit_ind:next_ind] if x.value]
                next_text = ' '.join(next_arr)
                my_dict[pattern_variable] = next_text
                unit_ind = next_ind
    
        result = pc_type(my_dict)

        return result

