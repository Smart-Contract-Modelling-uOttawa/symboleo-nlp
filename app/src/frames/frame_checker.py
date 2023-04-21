from typing import List
from app.classes.selection.selected_node import SelectedNode
from app.classes.frames.frame import Frame
from app.src.frames.inner_frame_checker import IInnerFrameChecker
from app.src.frames.frame_builder import IBuildFrames

class ICheckFrames:
    def get_frame(self, node_list: List[SelectedNode]) -> Frame:
        raise NotImplementedError()

# Kill this.
class FrameChecker(ICheckFrames):
    def __init__(
            self, 
            frame_list: List[Frame],
            inner_checker: IInnerFrameChecker,
            frame_builder: IBuildFrames
        ):
        self.__frame_list = frame_list
        self.__inner_checker = inner_checker
        self.__frame_builder = frame_builder

    def get_frame(self, node_list: List[SelectedNode]) -> Frame:
        frames = self._check_all_frames(node_list)
        if len(frames) > 1:
            raise ValueError('Too many potential frames')
        if len(frames) == 0:
            raise ValueError('No frames found')
        return frames[0]   


    def _check_all_frames(self, node_list: List[SelectedNode]) -> List[Frame]:
        results: List[Frame] = []

        for frame in self.__frame_list:
            if self.__inner_checker.check_frame(node_list, frame.pattern):
                next_frame = self.__frame_builder.build(frame, node_list)

                if next_frame.is_complete():
                    results.append(next_frame)
        
        return results

