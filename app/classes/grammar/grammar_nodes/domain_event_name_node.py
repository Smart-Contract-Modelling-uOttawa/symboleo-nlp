from typing import List
from app.classes.grammar.abstract_node import AbstractNode
from app.classes.grammar.node_type import NodeType

class DomainEventNameNode(AbstractNode):
    def __init__(self, id: str, children: List[AbstractNode] = [], init_value:str = ''):
        super().__init__(id, children)
        self.prompt = init_value
        self.node_type = NodeType.DOMAIN_EVENT_NAME
        self.init_value = init_value

    def get_value(self):
        return self.init_value    

