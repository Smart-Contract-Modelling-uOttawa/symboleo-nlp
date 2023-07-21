from __future__ import annotations
from typing import List
from app.classes.helpers.list_eq import ClassHelpers

class GrammarNode:
    def __init__(self, name:str, children: List[GrammarNode] = None):
        self.name = name
        self.children = children or []
    
    def __eq__(self, other: GrammarNode) -> bool:
        return self.name == other.name and \
            ClassHelpers.lists_eq(self.children, other.children, 'name')