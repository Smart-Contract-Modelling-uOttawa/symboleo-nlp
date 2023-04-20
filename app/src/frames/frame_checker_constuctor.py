from app.src.frames.frame_checker import FrameChecker
from app.src.frames.inner_frame_checker import InnerFrameChecker
from app.src.frames.frame_builder import FrameBuilder
from app.classes.frames.all_frames import get_all_frames
# Kill this
class FrameCheckerConstructor:
    @staticmethod
    def construct() -> FrameChecker:
        frame_list = get_all_frames()
        inner_checker = InnerFrameChecker()
        frame_builder = FrameBuilder()
        result = FrameChecker(frame_list, inner_checker, frame_builder)
        return result

