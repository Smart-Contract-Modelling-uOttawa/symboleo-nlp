from app.classes.selection.selected_node import SelectedNode, Basket
from app.classes.tokens.node_type import NodeType
from app.classes.frames.frame import Frame
from app.classes.frames.all_frames import *

from app.classes.spec.sym_event import VariableEvent

class DomainEventNameNode(SelectedNode):
    node_type = NodeType.DOMAIN_EVENT_NAME

    def build_frame(self, frame: Frame) -> Frame:
        new_frame = Frame.copy(frame)

        if isinstance(new_frame, BeforeEventFrame) or \
            isinstance(new_frame, AfterEventFrame) or \
            isinstance(new_frame, WithinTimespanEventFrame) or \
            isinstance(new_frame, UntilEventFrame) or \
            isinstance(new_frame, IfEventFrame):
            new_frame.subject = self.value
            new_frame.verb = 'completed'
        
        return new_frame


    def to_obj(self, basket: Basket):
        return VariableEvent(self.value)