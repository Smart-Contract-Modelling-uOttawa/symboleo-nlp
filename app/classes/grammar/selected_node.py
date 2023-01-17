from __future__ import annotations
from app.classes.grammar.node_type import NodeType
from app.classes.frames.frame import Frame
from app.classes.spec.sym_event import SymEvent


class SelectedNode:
    node_type: NodeType = None
    parent: SelectedNode = None
    child: SelectedNode = None
    ind: int = 0

    def __init__(
        self, 
        id:str,
        value: str = ''
    ):
        self.id = id
        self.value = value
    
    def build_frame(self, frame: Frame) -> Frame:
        return frame

    def to_obj(self, default_event: SymEvent = None):
        raise NotImplementedError()
    
