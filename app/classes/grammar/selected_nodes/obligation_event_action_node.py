from app.classes.grammar.selected_node import SelectedNode
from app.classes.grammar.node_type import NodeType
from app.classes.frames.frame import Frame
from app.classes.frames.all_frames import *

class ObligationEventActionNode(SelectedNode):
    node_type = NodeType.OBLIGATION_EVENT_ACTION

    def build_frame(self, frame: Frame) -> Frame:
        new_frame = Frame.copy(frame)

        if isinstance(new_frame, BeforeEventFrame) or \
            isinstance(new_frame, WithinTimespanEventFrame):
            new_frame.verb = self.value
        
        return new_frame


    def to_obj(self):
        return self.value
