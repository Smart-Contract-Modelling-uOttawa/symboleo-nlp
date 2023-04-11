from typing import List
from app.classes.tokens.abstract_node import AbstractNode
from app.classes.tokens.node_type import NodeType

class ContractEventNode(AbstractNode):
    def __init__(self, id: str, children: List[AbstractNode] = []):
        super().__init__(id, children)
        self.prompt = 'Contract Event'
        self.node_type = NodeType.CONTRACT_EVENT

    # No value to get on this
    def get_value(self):
        return None
