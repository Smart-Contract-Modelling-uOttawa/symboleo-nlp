from app.classes.selection.selected_node import SelectedNode
from app.classes.tokens.node_type import NodeType
from app.classes.frames.frame import Frame
from app.classes.other.frame_event import FrameEvent
from app.classes.frames.all_frames import *

class ContractSubjectNode(SelectedNode):
    node_type = NodeType.CONTRACT_SUBJECT

    def build_frame(self, frame: Frame) -> Frame:
        new_frame = Frame.copy(frame)
        if is_event_frame(new_frame):
            fe: FrameEvent = new_frame.frame_event 
            fe.subj = self.value
        
        return new_frame
