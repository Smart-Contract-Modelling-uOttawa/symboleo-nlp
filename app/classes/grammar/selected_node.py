from __future__ import annotations
from app.classes.grammar.node_type import NodeType
from app.classes.frames.frame import Frame
from app.classes.spec.sym_event import SymEvent
from app.classes.spec.contract_spec import Norm

# class in which we can pass objects that are needed for constructing new objects 
class Basket:
    default_event: SymEvent
    initial_norm: Norm

class SelectedNode:
    node_type: NodeType = None
    parent: SelectedNode = None
    child: SelectedNode = None
    ind: int = -1

    def __init__(
        self, 
        id:str,
        ind: int,
        value: str = '',
    ):
        self.id = id
        self.ind = ind
        self.value = value
    
    def build_frame(self, frame: Frame) -> Frame:
        return frame

    def to_obj(self, basket: Basket = None):
        raise NotImplementedError()

class DummyNode(SelectedNode):
    node_type = NodeType.DUMMY

    def to_obj(self, default_event: SymEvent):
        return 'dummy'