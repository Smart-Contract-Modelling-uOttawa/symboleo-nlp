from typing import List, Tuple, Dict
from app.classes.grammar.g_and import GAnd
from app.classes.grammar.g_or import GOr
from app.classes.grammar.full_grammar import PV, UnitType, GrammarUnit


class ICheckRecursivePattern:
    def check(self, units: List[UnitType], unit_ind: int, pattern_obj:GrammarUnit) -> Tuple[bool, int]:
        raise NotImplementedError()

class RecursivePatternChecker(ICheckRecursivePattern):
    def __init__(self, grammar: Dict[PV, GrammarUnit]):
        self.__grammar = grammar

    def check(self, units: List[UnitType], unit_ind: int, pattern_obj:GrammarUnit) -> Tuple[bool, int]:
        # Do a preliminary check for out of bounds
        if unit_ind >= len(units):
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
            return self.check(units, unit_ind, self.__grammar[pattern_obj])

        elif isinstance(pattern_obj, GAnd):
            check_a, next_ind = self.check(units, unit_ind, pattern_obj.a)
            if not check_a:
                return (False, unit_ind)
            
            check_b, next_ind = self.check(units, next_ind, pattern_obj.b)
            if check_b:
                return (True, next_ind)

        return (False, unit_ind)


