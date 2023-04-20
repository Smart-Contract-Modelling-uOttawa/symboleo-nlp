from typing import List, Dict, Type
from app.classes.selection.selected_node import SelectedNode
from app.classes.frames.frame import Frame

from app.src.frames.frame_getter import IGetFrame
from app.src.frame_updaters.frame_updater import IUpdateFrame

class IBuildFrames:
    def build(self, node_list: List[SelectedNode]) -> Frame:
        raise NotImplementedError()

class FrameBuilder(IBuildFrames):
    def __init__(
        self, 
        frame_getter: IGetFrame,
        updater_dict: Dict[Type[SelectedNode], IUpdateFrame]
    ):
        self.__frame_getter = frame_getter
        self.__updater_dict = updater_dict


    def build(self, node_list: List[SelectedNode]) -> Frame:
        frame = self.__frame_getter.get_frame(node_list)

        for node in node_list:
            updater = self.__updater_dict[type(node)]
            updater.update_frame(node, frame)
        
        return frame
