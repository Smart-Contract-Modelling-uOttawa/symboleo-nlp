from typing import List
from app.classes.units.all_units import *

from app.classes.pattern_classes.pattern_class import *
from app.classes.pattern_classes.pattern_variables import PatternVariable as PV
from app.classes.grammar.pattern_values import *

from app.src.pattern_builder.pattern_class_getter import IGetAllPatternClasses

class IExtractPatternClass:
    def extract(self, set_to_check: List[UnitType]) -> List[PatternClass]:
        raise NotImplementedError()
    
# TODO: Break this up. Very complex
## Might even put some in the grammar builder. Tree-like operations
class PatternClassExtractor(IExtractPatternClass):
    def __init__(
        self,
        all_pattern_class_getter: IGetAllPatternClasses
    ):
        self.__all_pattern_class_getter = all_pattern_class_getter

        # May want a better way of doing this...
        self._optional_pv = [PV.ADV_AND_PP]

    def extract(self, set_to_check: List[UnitType]) -> List[PatternClass]:
        result_set = []
        all_classes = self.__all_pattern_class_getter.get()
        for pattern_class in all_classes:
            if self._inner_check(set_to_check, pattern_class.sequence):
                result_set.append(pattern_class)

        if len(result_set) == 0:
            raise ValueError('No pattern classes found')
    
        return result_set     

    
    def _inner_check(self, set_to_check: List[UnitType], target_set: List[PV]):
        if len(set_to_check) < len(target_set):
            return False
        
        unit_ind = 0

        for pattern_variable in target_set:
            pattern_obj = temp_tree[pattern_variable]
            check, unit_ind = self._check_unit_pattern2(set_to_check, unit_ind, pattern_obj)

            if not check:
                return False

        return True


    # COMPLEX
    def _check_unit_pattern2(self, units: List[UnitType], unit_ind: int, pattern_obj:any):
        # Do a preliminary check for out of bounds
        # OK if we have a final node option
        if unit_ind >= len(units):
            if isinstance(pattern_obj, PV) and pattern_obj in self._optional_pv:
                return (True, unit_ind + 1)
        
        
        unit = units[unit_ind]

        if isinstance(pattern_obj, UnitType):
            if unit.name == pattern_obj.name:
                return (True, unit_ind + 1)
            else:
                return (False, unit_ind)

        elif isinstance(pattern_obj, GOr):
            for x in pattern_obj.args:
                next_check, next_ind = self._check_unit_pattern2(units, unit_ind, x)
                if next_check:
                    return (True, next_ind)
                
            return (False, unit_ind)
        
        elif isinstance(pattern_obj, PV):
            return self._check_unit_pattern2(units, unit_ind, temp_tree[pattern_obj])

        elif isinstance(pattern_obj, GAnd):
            check_a, next_ind = self._check_unit_pattern2(units, unit_ind, pattern_obj.a)
            if not check_a:
                return (False, unit_ind)
            
            check_b, next_ind = self._check_unit_pattern2(units, next_ind, pattern_obj.b)
            if check_b:
                return (True, next_ind)

        else: 
            return (False, unit_ind)


