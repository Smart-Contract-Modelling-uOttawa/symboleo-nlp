from typing import List, Tuple
from app.classes.grammar.pattern_values import PV, UnitType
from app.classes.grammar.pattern_values import GAnd, GOr, temp_tree


class ICheckRecursivePattern:
    def check(self, units: List[UnitType], unit_ind: int, pattern_obj:any) -> Tuple[bool, int]:
        raise NotImplementedError()

class RecursivePatternChecker(ICheckRecursivePattern):
    def __init__(self):
        self._tree = temp_tree
        # May want a better way of doing this...
        self._optional_pv = [PV.ADV_AND_PP]


    def check(self, units: List[UnitType], unit_ind: int, pattern_obj:any) -> Tuple[bool, int]:
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
                next_check, next_ind = self.check(units, unit_ind, x)
                if next_check:
                    return (True, next_ind)
                
            return (False, unit_ind)
        
        elif isinstance(pattern_obj, PV):
            return self.check(units, unit_ind, temp_tree[pattern_obj])

        elif isinstance(pattern_obj, GAnd):
            check_a, next_ind = self.check(units, unit_ind, pattern_obj.a)
            if not check_a:
                return (False, unit_ind)
            
            check_b, next_ind = self.check(units, next_ind, pattern_obj.b)
            if check_b:
                return (True, next_ind)

        else: 
            return (False, unit_ind)

