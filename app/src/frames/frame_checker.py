from typing import List
from app.classes.grammar.selected_node import SelectedNode
from app.classes.frames.frame import Frame
from app.src.frames.inner_frame_checker import IInnerFrameChecker
from app.src.frames.frame_builder import IBuildFrames

class ICheckFrames:
    def check_frames(self, node_list: List[SelectedNode]):
        raise NotImplementedError()


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

    def check_all_frames(self, node_list: List[SelectedNode]) -> List[Frame]:
        results: List[Frame] = []

        for frame in self.__frame_list:
            if self.__inner_checker.check_frame(node_list, frame.pattern):
                next_frame = self.__frame_builder.build(frame, node_list)

                if next_frame.is_complete():
                    results.append(next_frame)
        
        return results

