from app.classes.selection.selected_node import SelectedNode
from app.classes.tokens.node_type import NodeType
from app.classes.frames.frame import Frame
from app.classes.frames.all_frames import *

class DomainTimepointNode(SelectedNode):
    node_type = NodeType.DOMAIN_TIMEPOINT

    def build_frame(self, frame: Frame) -> Frame:
        new_frame = Frame.copy(frame)

        if isinstance(new_frame, BeforeTimePointFrame):
            new_frame.timepoint = self.value
        
        return new_frame
