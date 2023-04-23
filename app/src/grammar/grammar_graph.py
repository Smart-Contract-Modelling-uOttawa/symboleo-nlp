from typing import List
from app.classes.tokens.abstract_node import AbstractNode
from app.classes.frames.frame import Frame
from app.classes.tokens.node_type import NodeType

class IGrammarGraph:
    def get_children(self, node: AbstractNode) -> List[AbstractNode]:
        raise NotImplementedError()

# TODO: This will be much more complex... Might pass in contract, previous value, etc...
# For example, depending on the verb type, we may only want to show one type of child
# Would require some validation on the input. Doable.
class GrammarGraph(IGrammarGraph):
    def __init__(self, frames: List[Frame] = None):
        self.s = 0 
        self.in_common_event_mode = False

    def get_children(self, node: AbstractNode) -> List[AbstractNode]:
        result = [x() for x in node.children]
        
        if node.node_type == NodeType.COMMON_EVENT:
            self.in_common_event_mode = True
            self.common_pattern = None # Get the pattern!
        
        #if self.in_common_event_mode:
            # Find where we are in the pattern
            # Subj, Verb, Dobj, Adverb
            # Suppose we need the subject
            


        
        
        return result
    

    
        # OK. So lets think about the CommonEvents
        ## If the node type is a common event, we'll get a value as well
        ### Then:......
        ## Fetch the thing we need
        ## Its almost like we need to turn a switch on
