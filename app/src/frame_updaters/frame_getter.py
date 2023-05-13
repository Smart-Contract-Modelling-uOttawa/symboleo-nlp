from typing import List
from app.classes.selection.selected_node import SelectedNode
from app.classes.frames.frame import Frame
from app.src.frame_updaters.all_frames_getter import IGetAllFrames
from app.src.frame_updaters.inner_frame_checker import IInnerFrameChecker

class IGetFrame:
    def get_frame(self, node_list: List[SelectedNode]) -> Frame:
        raise NotImplementedError()

class FrameGetter(IGetFrame):
    def __init__(
            self, 
            all_frames_getter: IGetAllFrames,
            inner_checker: IInnerFrameChecker,
        ):
        self.__all_frames_getters = all_frames_getter
        self.__inner_checker = inner_checker

    def get_frame(self, node_list: List[SelectedNode]) -> Frame:
        frames = []
        all_frames = self.__all_frames_getters.get()
        for f in all_frames:
            res = self.__inner_checker.check_frame(node_list, f.pattern)
            if res:
                frames.append(f)
        
        if len(frames) > 1:
            frame_list = ','.join([str(type(x)) for x in frames])
            raise ValueError(f'Too many potential frames: {frame_list}')
        if len(frames) == 0:
            raise ValueError('No frames found')
        return frames[0]   
