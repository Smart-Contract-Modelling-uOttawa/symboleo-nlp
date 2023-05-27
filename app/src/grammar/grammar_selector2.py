from typing import List, Dict, Type
from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.units.node_type import NodeType
from app.classes.units.input_unit import InputUnit
from app.classes.units.root_node import RootNode as RootToken

from app.classes.selection.selected_node import SelectedNode
from app.classes.selection.root_node import RootNode

from app.src.grammar.token_selector import ISelectToken
from app.src.grammar.token_processor import IProcessToken

class ISelectGrammar:
    def select(self):
        raise NotImplementedError()
# Kill this
class ISelectGrammarNodes:
    def select(self, node_set: List[InputUnit]) -> InputUnit:
        raise NotImplementedError()

class GrammarSelector(ISelectGrammar):
    def __init__(
        self, 
        token_selector: ISelectToken,
        token_processor: IProcessToken
    ):
        self.__token_selector = token_selector
        self.__token_processor = token_processor

    def select(self, contract: ISymboleoContract) -> List[SelectedNode]:
        chosen_token = RootToken()
        results: List[SelectedNode] = [RootNode()]
        next_node = None

        while (True):
            chosen_token = self.__token_selector.select(chosen_token, contract, next_node)

            next_node = self.__token_processor.process(chosen_token, contract) # pass in contract, etc...

            results.append(next_node)

            if next_node.node_type == NodeType.FINAL_NODE:
                break
            
        return results
