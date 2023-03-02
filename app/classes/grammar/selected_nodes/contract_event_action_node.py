from app.classes.grammar.selected_node import SelectedNode
from app.classes.grammar.node_type import NodeType
from app.classes.spec.sym_event import SymEvent
from app.classes.frames.frame import Frame
from app.classes.frames.all_frames import *

class ContractEventActionNode(SelectedNode):
    node_type = NodeType.CONTRACT_EVENT_ACTION

    # Will make this typed more strongly...
    def build_frame(self, frame: Frame) -> Frame:
        new_frame = Frame.copy(frame)

        if isinstance(new_frame, BeforeEventFrame) or \
            isinstance(new_frame, AfterEventFrame):
            new_frame.verb = self.value
            new_frame.subject = 'the contract'
        
        elif isinstance(new_frame, WithinTimespanEventFrame):
            new_frame.verb = self.value
            new_frame.subject = 'the contract'
        
        elif isinstance(new_frame, IfEventFrame):
            new_frame.verb = self.value
            new_frame.subject = 'the contract'
        
        return new_frame


    def to_obj(self, default_event: SymEvent):
        return self.value