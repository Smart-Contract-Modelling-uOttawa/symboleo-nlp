from typing import List
from app.classes.tokens.abstract_node import AbstractNode
from app.classes.frames.frame import Frame

class IGrammarGraph:
    def get_children(self, node: AbstractNode) -> List[AbstractNode]:
        raise NotImplementedError()

# TODO: This will be much more complex... Might pass in contract, previous value, etc...
# For example, depending on the verb type, we may only want to show one type of child
# Would require some validation on the input. Doable.
class GrammarGraph(IGrammarGraph):
    def __init__(self, frames: List[Frame] = None):
        self.s = 0 

    def get_children(self, node: AbstractNode) -> List[AbstractNode]:
        result = [x() for x in node.children]
        return result
