from typing import List
from app.classes.tokens.abstract_node import AbstractNode
from app.classes.frames.frame import Frame

class IGrammarGraph:
    def get_children(self, node: AbstractNode) -> List[AbstractNode]:
        raise NotImplementedError()

class GrammarGraph(IGrammarGraph):
    def __init__(self, frames: List[Frame] = None):
        self.s = 0 
        # Might want the contract though...
        ## Or maybe thats passed in on get_children. Because it updates
        # Graph construction...
        # BUT - the frames are minimal... How do we move beyond that..
        # May use it. May not.

    def get_children(self, node: AbstractNode) -> List[AbstractNode]:
        result = [x() for x in node.children]
        return result
