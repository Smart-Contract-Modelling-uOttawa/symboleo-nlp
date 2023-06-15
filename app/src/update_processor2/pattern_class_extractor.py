from typing import List
from app.classes.units.all_units import *

from app.classes.patterns.pattern_classes import *

from app.src.update_processor2.pattern_class_getter import IGetAllPatternClasses

class IExtractPatternClass:
    def extract(self, set_to_check: List[UnitType]) -> PatternClass:
        raise NotImplementedError()
    

class PatternClassExtractor(IExtractPatternClass):
    def __init__(
        self,
        all_pattern_class_getter: IGetAllPatternClasses
    ):
        self.__all_pattern_class_getter = all_pattern_class_getter

    def extract(self, set_to_check: List[UnitType]) -> PatternClass:
        result_set = []
        all_classes = self.__all_pattern_class_getter.get()
        for pattern_class in all_classes:
            if self._inner_check(set_to_check, pattern_class.sequence):
                result_set.append(pattern_class)

        if len(result_set) == 0:
            raise ValueError('No pattern classes found')
        if len(result_set) > 1:
            raise ValueError('Multiple patterns found')

        return result_set[0]        

    
    def _inner_check(self, set_to_check: List[UnitType], target_set: List[PT]):
        if len(set_to_check) < len(target_set):
            return False
        
        for i, pattern_token in enumerate(target_set):
            next_unit = set_to_check[i]
            if next_unit not in pt_value_dict[pattern_token]:
                return False
        
        return True

