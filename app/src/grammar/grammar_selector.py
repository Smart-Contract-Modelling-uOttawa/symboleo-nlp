from typing import List
from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.selection.selected_node import SelectedNode
from app.classes.tokens.node_type import NodeType
from app.classes.tokens.abstract_node import AbstractNode

from app.src.operations.input_converter import IConvertInput
from app.classes.tokens.root_node import RootNode

from app.src.grammar.grammar_graph import IGrammarGraph
from app.src.grammar.value_getter import IGetValues

class ISelectGrammar:
    def select(self):
        raise NotImplementedError()

class ISelectGrammarNodes:
    def select(self, node_set: List[AbstractNode]) -> AbstractNode:
        raise NotImplementedError()


class GrammarSelector(ISelectGrammar):
    def __init__(
        self, 
        graph: IGrammarGraph,
        value_getter: IGetValues,
        input_converter: IConvertInput,
        inner_selector: ISelectGrammarNodes
    ):
        self.__graph = graph
        self.__value_getter = value_getter
        self.__input_converter = input_converter
        self.__inner_selector = inner_selector

    def select(self, contract: ISymboleoContract) -> List[SelectedNode]:
        curr = RootNode()
        results: List[SelectedNode] = [curr.sn_type()]

        while (True):
            next_set = self.__graph.get_children(curr)
            if len(next_set) == 0: 
                break

            curr = self.__inner_selector.select(next_set)
            
            value = self.__value_getter.get(curr)
            next_result = self.__input_converter.convert([value])[0]
            
            results.append(next_result)
            
        return results
