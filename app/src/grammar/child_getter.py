from typing import Dict, Type, List
from app.classes.units.input_unit import InputUnit
from app.classes.selection.selected_node import SelectedNode
from app.classes.spec.symboleo_contract import SymboleoContract

from app.src.child_getters.child_getter import IGetNodeChildren

class IGetChildren:
    def get(self, unit: InputUnit, element: SelectedNode, contract: SymboleoContract) -> List[InputUnit]:
        raise NotImplementedError()

class ChildGetter(IGetChildren):
    def __init__(self, child_getter_dict: Dict[Type[InputUnit], IGetNodeChildren]):
        self.__dict = child_getter_dict
    
    def get(self, unit: InputUnit, element: SelectedNode, contract: SymboleoContract) -> List[InputUnit]:
        op = self.__dict[type(unit)]
        return op.get(unit, contract, element)