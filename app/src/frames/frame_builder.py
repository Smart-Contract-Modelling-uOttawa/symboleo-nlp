import copy
from typing import List
from app.classes.selection.selected_node import SelectedNode
from app.classes.frames.frame import Frame

# This assumes the node_list matches the frame pattern
class IBuildFrames:
    def build(self, frame: Frame, node_list: List[SelectedNode]) -> Frame:
        raise NotImplementedError()


class FrameBuilder(IBuildFrames):
    def build(self, frame: Frame, node_list: List[SelectedNode]) -> Frame:
        new_frame = copy.deepcopy(frame)
        for node in node_list:
            new_frame = node.build_frame(new_frame)
        
        return new_frame
