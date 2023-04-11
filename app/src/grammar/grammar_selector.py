from app.classes.tokens.abstract_node import AbstractNode
from app.src.grammar.selection import Selection

class ISelectGrammar:
    def select(self, root: AbstractNode) -> Selection:
        raise NotImplementedError()

class ISelectGrammarNodes:
    def select(self, target: AbstractNode) -> AbstractNode:
        raise NotImplementedError()

class GrammarSelector(ISelectGrammar):
    def __init__(self, node_selector: ISelectGrammarNodes):
        self.__node_selector: ISelectGrammarNodes = node_selector

    def select(self, root_node: AbstractNode) -> Selection:
        result = Selection()
        target = root_node
        result.add_node(target)

        while(len(target.children) > 0):
            target = self.__node_selector.select(target)
            value = target.get_value()
            result.add_node(target, value)
        
        return result
