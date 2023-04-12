from __future__ import annotations
from app.classes.tokens.node_type import NodeType
from app.classes.frames.frame import Frame
from app.classes.spec.sym_event import SymEvent
from app.classes.spec.norm import Norm
from app.classes.selection.selection_tools import SelectionTools

# TODO: Might be able to get rid of this..
# class in which we can pass objects that are needed for constructing new objects 
class Basket:
    default_event: SymEvent
    initial_norm: Norm

# I think I'll need to inject some sort of general interface into this
## For handling NLP and other operations
class SelectedNode: # pragma: no cover
    node_type: NodeType = None
    parent: SelectedNode = None
    child: SelectedNode = None
    ind: int = -1
    tools: SelectionTools = None

    def __init__(
        self, 
        id:str,
        ind: int,
        value: str = '',
        tools: SelectionTools = None
    ):
        self.id = id
        self.ind = ind
        self.value = value
        self.tools = tools or SelectionTools.build()
    
    def build_frame(self, frame: Frame) -> Frame:
        return frame

    def to_obj(self, basket: Basket = None):
        raise NotImplementedError()

class DummyNode(SelectedNode):
    node_type = NodeType.DUMMY

    def to_obj(self, default_event: SymEvent):
        return 'dummy'