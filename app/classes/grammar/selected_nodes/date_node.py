from app.classes.grammar.selected_node import SelectedNode, Basket
from app.classes.grammar.node_type import NodeType
from app.classes.frames.frame import Frame
from app.classes.frames.all_frames import *

from app.classes.spec.sym_point import PointVDE

class DateNode(SelectedNode):
    node_type = NodeType.DATE

    def build_frame(self, frame: Frame) -> Frame:
        new_frame = Frame.copy(frame)

        if isinstance(new_frame, BeforeDateFrame) or \
            isinstance(new_frame, AfterDateFrame):
            new_frame.date_text = self.value
        
        return new_frame


    def to_obj(self, basket: Basket):
        return PointVDE(self.value)