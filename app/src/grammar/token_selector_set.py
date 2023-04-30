from typing import List
from app.classes.tokens.abstract_node import AbstractNode

class ISelectTokenFromSet:
    def select(self, node_set: List[AbstractNode]) -> AbstractNode:
        raise NotImplementedError()
