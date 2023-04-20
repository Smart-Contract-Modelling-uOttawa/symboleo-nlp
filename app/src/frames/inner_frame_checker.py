from typing import List
from app.classes.selection.selected_node import SelectedNode
from app.classes.tokens.node_type import NodeType

class IInnerFrameChecker:
    def check_frame(self, node_list: List[SelectedNode], frame_pattern: List[NodeType]) -> bool:
        raise NotImplementedError()

class InnerFrameChecker(IInnerFrameChecker):
    # This function does NOT care about frames that may still be possible. . If needed, that will be separate
    def check_frame(self, node_list: List[SelectedNode], frame_pattern: List[NodeType]) -> bool:
        
        nt = [x.node_type for x in node_list]

        # If the frame pattern is longer than the node list, then we are not there yet
        if len(frame_pattern) > len(nt):
            return False
        
        for i in range(len(frame_pattern)):
            if frame_pattern[i] != nt[i]:
                return False
        
        return True
    