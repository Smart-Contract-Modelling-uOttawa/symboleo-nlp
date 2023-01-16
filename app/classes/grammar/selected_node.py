from __future__ import annotations
from app.classes.grammar.node_type import NodeType


class SelectedNode:
    node_type: NodeType = None
    parent: SelectedNode = None
    child: SelectedNode = None
    user_text: str = None

    def __init__(
        self, 
        id:str,
        parent: SelectedNode,
        value: str = '',
        ind: int = 0
    ):
        self.id = id
        self.parent = parent
        self.value = value
        self.ind = ind
    
    # Need to set the child retroactively. Not ideal...
    def add_child(self, node: SelectedNode):
        self.child = node
    
    def to_user_text(self) -> str:
        raise NotImplementedError()

    def to_obj(self):
        raise NotImplementedError()
