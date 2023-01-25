from typing import List
from app.classes.grammar.abstract_node import AbstractNode
from app.classes.grammar.node_type import NodeType

class StateNode(AbstractNode):
    def __init__(self, id: str, children: List[AbstractNode] = []):
        super().__init__(id, children)
        self.prompt = 'Describe a state'
        self.node_type = NodeType.STATE

    def get_value(self):
        return None
