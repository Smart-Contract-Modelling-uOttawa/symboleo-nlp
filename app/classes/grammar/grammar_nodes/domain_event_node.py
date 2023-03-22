from typing import List
from app.classes.grammar.abstract_node import AbstractNode
from app.classes.grammar.node_type import NodeType

class DomainEventNode(AbstractNode):
    def __init__(self, id: str, children: List[AbstractNode] = []):
        super().__init__(id, children)
        self.prompt = 'Domain event' # Not a fan of this... assumes the user knows what a domain is...
        self.node_type = NodeType.DOMAIN_EVENT

    # No value to get on this
    def get_value(self):
        return None
