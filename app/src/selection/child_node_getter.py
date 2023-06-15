from typing import Dict, Type, List
from app.classes.units.input_unit import InputUnit
from app.classes.spec.symboleo_contract import SymboleoContract

from app.src.selection.child_getters.child_getter import IGetUnitChildren

class IGetNodeChildren:
    def get(self, unit: InputUnit, contract: SymboleoContract) -> List[InputUnit]:
        raise NotImplementedError()

class ChildNodeGetter(IGetNodeChildren):
    def __init__(self, child_getter_dict: Dict[Type[InputUnit], IGetUnitChildren]):
        self.__dict = child_getter_dict
    
    def get(self, unit: InputUnit, contract: SymboleoContract) -> List[InputUnit]:
        op = self.__dict[type(unit)]
        return op.get(unit, contract)