from app.classes.grammar.selected_node import SelectedNode, Basket
from app.classes.grammar.node_type import NodeType
from app.classes.frames.frame import Frame
from app.classes.frames.all_frames import *

class TimepointNode(SelectedNode):
    node_type = NodeType.TIMEPOINT

    def to_obj(self, basket: Basket):
        return self.child.to_obj(basket)