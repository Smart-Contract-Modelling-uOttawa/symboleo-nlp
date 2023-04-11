from typing import List
from app.classes.tokens.abstract_node import AbstractNode
from app.classes.tokens.node_type import NodeType

class ObligationEventNode(AbstractNode):
    def __init__(self, id: str, children: List[AbstractNode] = []):
        super().__init__(id, children)
        self.prompt = 'Obligation Event'
        self.node_type = NodeType.OBLIGATION_EVENT

    def get_value(self):
        return None
