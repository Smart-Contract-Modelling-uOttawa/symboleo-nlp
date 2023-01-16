from __future__ import annotations
from typing import List
from app.classes.grammar.node_type import NodeType

# Might have a flag that denotes if a value is needed or not...
class AbstractNode:
    id: str = None
    node_type: NodeType = None
    prompt: str = None
    children: List[AbstractNode] = []
    
    def __init__(self, id: str, children: List[AbstractNode] = []):
        self.id = id
        self.children = children
    
    def get_value(self):
        raise NotImplementedError()