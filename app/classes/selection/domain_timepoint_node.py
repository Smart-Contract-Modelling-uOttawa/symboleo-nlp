from app.classes.selection.selected_node import SelectedNode, Basket
from app.classes.tokens.node_type import NodeType
from app.classes.frames.frame import Frame
from app.classes.frames.all_frames import *

from app.classes.spec.sym_point import PointVDE

class DomainTimepointNode(SelectedNode):
    node_type = NodeType.DOMAIN_TIMEPOINT

    # Will make this typed more strongly...
    def build_frame(self, frame: Frame) -> Frame:
        new_frame = Frame.copy(frame)

        if isinstance(new_frame, BeforeTimePointFrame):
            new_frame.timepoint = self.value
        
        return new_frame


    def to_obj(self, basket: Basket):
        return PointVDE(self.value)