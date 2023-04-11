from typing import List
from app.classes.tokens.abstract_node import AbstractNode
from app.classes.tokens.node_type import NodeType

class IfNode(AbstractNode):
    def __init__(self, id: str, children: List[AbstractNode] = []):
        super().__init__(id, children)
        self.prompt = 'if'
        self.node_type = NodeType.IF
    
    def get_value(self):
        return 'if'
