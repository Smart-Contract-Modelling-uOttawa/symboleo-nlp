from __future__ import annotations
from typing import TypeVar, Generic
from app.classes.units.node_type import NodeType

T = TypeVar('T')

class SelectedNode(Generic[T]): # pragma: no cover
    node_type: NodeType = None

    def __init__(self, value: T = None):
        self.value = value

class DummyNode(SelectedNode):
    node_type = NodeType.DUMMY
