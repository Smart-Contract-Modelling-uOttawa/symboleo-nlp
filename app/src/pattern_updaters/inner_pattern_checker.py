from typing import List
from app.classes.elements.element import Element
from app.classes.units.unit_type import UnitType

class IInnerPatternChecker:
    def check_pattern(self, elements: List[Element], pattern_sequence: List[UnitType]) -> bool:
        raise NotImplementedError()

class InnerPatternChecker(IInnerPatternChecker):
    # This function does NOT care about patterns that MAY still be possible. 
    ## If needed, that will be separate
    def check_pattern(self, elements: List[Element], pattern_sequence: List[UnitType]) -> bool:
        nt = [x.unit_type for x in elements]

        # If the pattern is longer than the list, then we are not there yet
        if len(pattern_sequence) > len(nt):
            return False
        
        for i in range(len(pattern_sequence)):
            if pattern_sequence[i] != nt[i]:
                return False
        
        return True
    