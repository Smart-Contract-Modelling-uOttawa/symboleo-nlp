from typing import List, Dict, Type
from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.units.input_unit import InputUnit
from app.classes.selection.selected_node import SelectedNode
from app.classes.units.final_node import FinalNode

from app.src.child_getters.child_getter import IGetNodeChildren
from app.src.grammar.token_selector_set import ISelectTokenFromSet


class ISelectToken:
    def select(
        self, 
        chosen_token: InputUnit, 
        contract: ISymboleoContract, 
        prev_node: SelectedNode 
    ) -> InputUnit:
        raise NotImplementedError()

class TokenSelector(ISelectToken):
    def __init__(
        self, 
        child_getter_dict: Dict[Type[InputUnit], IGetNodeChildren],
        inner_selector: ISelectTokenFromSet
        
    ):
        self.__child_getter_dict = child_getter_dict
        self.__inner_selector = inner_selector

    def select(self, chosen_token: InputUnit, contract: ISymboleoContract, prev_node: SelectedNode) -> InputUnit: 
            op = self.__child_getter_dict[type(chosen_token)]
            next_set = op.get(chosen_token, contract, prev_node)
            if len(next_set) == 0: 
                return FinalNode()

            result = self.__inner_selector.select(next_set)

            return result


