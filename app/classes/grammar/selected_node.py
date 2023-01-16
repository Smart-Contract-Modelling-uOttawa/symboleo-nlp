from __future__ import annotations
from typing import List
from app.classes.grammar.node_type import NodeType
from app.classes.frames.frame import Frame


class SelectedNode:
    node_type: NodeType = None
    parent: SelectedNode = None
    child: SelectedNode = None
    user_text: str = None
    ind: int = 0

    def __init__(
        self, 
        id:str,
        value: str = ''
    ):
        self.id = id
        self.value = value
    
    # Decide how I use the frame... create a new node?
    # Don't pass in a frame. Pass in a FramePattern. 
    # then return the corresponding frame
    def build_frame(self, frame: Frame) -> Frame:
        return frame
    
    # Will remove this...
    def to_user_text(self) -> str:
        raise NotImplementedError()

    def to_obj(self):
        raise NotImplementedError()
    
    # Remove
    # Is this appropriate?
    # Should at least be returning a new list, rather than altering
    @staticmethod 
    def organize_list(node_list: List[SelectedNode]):
        for i, node in enumerate(node_list):
            node.ind = i
            
            if node.node_type != NodeType.ROOT:
                node.parent = node_list[i-1]
            
            if len(node_list) > i+1:
                node.add_child(node_list[i+1])
        
