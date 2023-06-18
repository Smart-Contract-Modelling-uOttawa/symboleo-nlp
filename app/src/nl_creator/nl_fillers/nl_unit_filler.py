from typing import List, Dict
import copy
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.patterns.pattern_classes import *
from app.classes.operations.user_input import UserInput

class IFillNLUnit:
    def fill(self, contract: SymboleoContract, curr: List[str], input_list: List[UserInput], i: int) -> List[str]:
        raise NotImplementedError()


# TODO: Move this somewhere else
value_dict: Dict[UnitType, str] = {
    UnitType.WITHIN: 'within',
    UnitType.IF: 'if',
    UnitType.OF: 'of',
    UnitType.FAILS_TO: 'fails to',
    UnitType.UNLESS: 'unless',
    UnitType.BEFORE: 'before',
}

class SkipFiller(IFillNLUnit):
    def fill(self, contract: SymboleoContract, curr: List[str], input_list: List[UserInput], i: int) -> List[str]:
        return copy.deepcopy(curr)

class DefaultNLFiller(IFillNLUnit):
    def fill(self, contract: SymboleoContract, curr: List[str], input_list: List[UserInput], i: int) -> List[str]:
        result = copy.deepcopy(curr)

        unit_type = input_list[i].unit_type
        val = input_list[i].value 

        if unit_type in value_dict:
            next_res = value_dict[unit_type]
            result.append(next_res)
        
        elif val and val != '':
            result.append(val)
        
        return result

