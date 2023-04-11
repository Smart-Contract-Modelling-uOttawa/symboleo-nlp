from app.classes.selection.selected_node import SelectedNode, Basket
from app.classes.tokens.node_type import NodeType
from app.classes.frames.frame import Frame
from app.classes.frames.all_frames import *

class ObligationEventVarNode(SelectedNode):
    node_type = NodeType.OBLIGATION_EVENT_VAR

    def build_frame(self, frame: Frame) -> Frame:
        new_frame = Frame.copy(frame)

        if isinstance(new_frame, BeforeEventFrame) or \
            isinstance(new_frame, AfterEventFrame) or\
            isinstance(new_frame, WithinTimespanEventFrame) or \
            isinstance(new_frame, UntilEventFrame) or \
            isinstance(new_frame, IfEventFrame):
            new_frame.subject = f'the {self.value} obligation'
        
        return new_frame


    def to_obj(self, basket: Basket):
        return self.value
