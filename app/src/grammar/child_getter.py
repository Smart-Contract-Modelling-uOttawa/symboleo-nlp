from typing import Dict, Type, List
from app.classes.tokens.abstract_node import AbstractNode
from app.classes.selection.selected_node import SelectedNode
from app.classes.spec.symboleo_contract import SymboleoContract

from app.src.child_getters.child_getter import IGetNodeChildren

class IGetChildren:
    def get(self, unit: AbstractNode, element: SelectedNode, contract: SymboleoContract) -> List[AbstractNode]:
        raise NotImplementedError()

class ChildGetter(IGetChildren):
    def __init__(self, child_getter_dict: Dict[Type[AbstractNode], IGetNodeChildren]):
        self.__dict = child_getter_dict
    
    def get(self, unit: AbstractNode, element: SelectedNode, contract: SymboleoContract) -> List[AbstractNode]:
        op = self.__dict[type(unit)]
        return op.get(unit, contract, element)