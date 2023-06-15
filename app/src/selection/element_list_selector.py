from typing import List
from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.units.root_unit import RootUnit
from app.classes.operations.user_input import UnitType, UserInput

from app.src.selection.child_node_getter import IGetNodeChildren
from app.src.selection.token_selector_set import ISelectNode
from app.src.selection.input_value_getter import IGetInputValues

# TODO: F3? - Will need to integrate the CommonEvent handling stuff in though...
class ISelectElementList:
    def select(self, contract: ISymboleoContract) -> List[UserInput]:
        raise NotImplementedError()
    
class ElementListSelector(ISelectElementList):
    def __init__(
        self, 
        child_node_getter: IGetNodeChildren,
        child_selector: ISelectNode,
        input_value_getter: IGetInputValues
    ):
        self.__child_node_getter = child_node_getter
        self.__child_selector = child_selector
        self.__value_getter = input_value_getter

    def select(self, contract: ISymboleoContract) -> List[UserInput]:
        unit = RootUnit()
        results: List[UserInput] = []

        while (True):
            children = self.__child_node_getter.get(unit, contract)

            if len(children) == 0:
                break
            elif len(children) == 1:
                unit = children[0]
            else:
                unit = self.__child_selector.select(children) # Involves user input
            
            input_value = self.__value_getter.get(unit) # Involves user input

            results.append(input_value)
        
        return results
