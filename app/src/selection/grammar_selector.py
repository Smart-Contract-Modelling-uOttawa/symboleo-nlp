from typing import List
from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.operations.user_input import UnitType, UserInput

from app.src.selection.child_getter import IGetChildren
from app.src.selection.token_selector_set import ISelectNode
from app.src.selection.input_value_getter import IGetInputValues

from app.src.grammar_builder.grammar_builder import GrammarNode

# TODO: F3? - Re-integrate this into console application
class ISelectElementList:
    def select(self, contract: ISymboleoContract) -> List[UserInput]:
        raise NotImplementedError()
    
class GrammarSelector(ISelectElementList):
    def __init__(
        self, 
        child_node_getter: IGetChildren,
        child_selector: ISelectNode,
        input_value_getter: IGetInputValues
    ):
        self.__child_node_getter = child_node_getter
        self.__child_selector = child_selector
        self.__value_getter = input_value_getter

    def select(self, contract: ISymboleoContract, root_node: GrammarNode) -> List[UserInput]:
        curr = root_node
        results: List[UserInput] = []

        while len(curr.children) > 0:
            children = self.__child_node_getter.get(curr, contract)

            if len(children) == 0:
                break
            elif len(children) == 1:
                unit = children[0]
            else:
                unit = self.__child_selector.select(children) # Involves user input
            
            input_value = self.__value_getter.get(unit) # Involves user input

            results.append(input_value)

            # TODO: Need to transform curr into a GrammarNode..
            curr = unit
        
        return results
