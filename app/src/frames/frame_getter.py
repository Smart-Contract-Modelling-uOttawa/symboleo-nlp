from typing import List
from app.classes.selection.selected_node import SelectedNode
from app.classes.frames.frame import Frame
from app.src.frames.inner_frame_checker import IInnerFrameChecker

class IGetFrame:
    def get_frame(self, node_list: List[SelectedNode]) -> Frame:
        raise NotImplementedError()

class FrameGetter(IGetFrame):
    def __init__(
            self, 
            frame_list: List[Frame],
            inner_checker: IInnerFrameChecker,
        ):
        self.__frame_list = frame_list
        self.__inner_checker = inner_checker

    def get_frame(self, node_list: List[SelectedNode]) -> Frame:
        frames = []
        for f in self.__frame_list:
            res = self.__inner_checker.check_frame(node_list, f.pattern)
            if res:
                frames.append(f)
        
        if len(frames) > 1:
            frame_list = ','.join([str(type(x)) for x in frames])
            raise ValueError(f'Too many potential frames: {frame_list}')
        if len(frames) == 0:
            raise ValueError('No frames found')
        return frames[0]   

    # Kill
    # def _check_all_frames(self, node_list: List[SelectedNode]) -> List[Frame]:
    #     results: List[Frame] = []

    #     for frame in self.__frame_list:
    #         if self.__inner_checker.check_frame(node_list, frame.pattern):
    #             next_frame = self.__frame_builder.build(frame, node_list)

    #             if next_frame.is_complete():
    #                 results.append(next_frame)
        
    #     return results

