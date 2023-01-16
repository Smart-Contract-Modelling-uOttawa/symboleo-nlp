from typing import List
from app.classes.grammar.abstract_node import AbstractNode
from app.classes.grammar.node_type import NodeType

class TimespanNode(AbstractNode):
    def __init__(self, id: str, children: List[AbstractNode] = []):
        super().__init__(id, children)
        self.prompt = 'Enter a timespan'
        self.node_type = NodeType.TIMESPAN

    def get_value(self):
        result = input('Enter a timespan (e.g. 2 weeks): ')    
        return result
        