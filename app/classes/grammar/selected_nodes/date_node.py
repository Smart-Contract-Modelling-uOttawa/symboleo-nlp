from app.classes.grammar.selected_node import SelectedNode
from app.classes.grammar.node_type import NodeType
from app.classes.frames.frame import Frame
from app.classes.frames.all_frames import *
from app.classes.spec.sym_event import SymEvent

from app.classes.spec.sym_point import PointVDE

class DateNode(SelectedNode):
    node_type = NodeType.DATE

    def build_frame(self, frame: Frame) -> Frame:
        new_frame = Frame.copy(frame)

        if isinstance(new_frame, BeforeDateFrame):
            new_frame.date_text = self.value
        
        return new_frame


    def to_obj(self, default_event: SymEvent):
        return PointVDE(self.value)