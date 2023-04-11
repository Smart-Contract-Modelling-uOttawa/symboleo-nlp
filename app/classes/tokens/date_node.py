from typing import List
from app.classes.tokens.abstract_node import AbstractNode
from app.classes.tokens.node_type import NodeType

class DateNode(AbstractNode):
    def __init__(self, id: str, children: List[AbstractNode] = []):
        super().__init__(id, children)
        self.prompt = 'Enter a date'
        self.node_type = NodeType.DATE

    def get_value(self):
        result = input('Enter a date (yyyy/mm/dd): ')
        return result
