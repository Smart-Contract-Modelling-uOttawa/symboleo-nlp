from __future__ import annotations
from app.classes.tokens.node_type import NodeType
from app.classes.frames.frame import Frame

class SelectedNode: # pragma: no cover
    node_type: NodeType = None

    def __init__(
        self,
        value: str = ''
    ):
        self.value = value

    def build_frame(self, frame: Frame) -> Frame:
        return frame


class DummyNode(SelectedNode):
    node_type = NodeType.DUMMY