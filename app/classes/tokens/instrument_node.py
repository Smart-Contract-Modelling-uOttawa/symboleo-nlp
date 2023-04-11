from typing import List
from app.classes.tokens.abstract_node import AbstractNode
from app.classes.tokens.node_type import NodeType

class InstrumentNode(AbstractNode):
    def __init__(self, id: str, children: List[AbstractNode] = []):
        super().__init__(id, children)
        self.prompt = 'Enter an instrument'
        self.node_type = NodeType.INSTRUMENT

    def get_value(self):
        # This is where we'll need NLP capabilities.
        ## What is going to be the best way to inject this in...
        ## Perhaps the Abstract node has the functionality?
        result = None
        is_valid = False

        while not is_valid:
            result = input('Enter an instrument (e.g. a van): ')    
            is_valid = self._validate_input(result)
        
        return result
    
    
    def _validate_input(self, user_input):
        return True