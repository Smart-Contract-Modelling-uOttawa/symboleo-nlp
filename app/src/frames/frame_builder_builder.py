from app.src.frames.inner_frame_checker import InnerFrameChecker
from app.src.frames.frame_getter import FrameGetter
from app.src.frames.frame_helper import FrameHelper
from app.src.frame_updaters.updater_dict import UpdaterDictConstructor
from app.src.frames.frame_builder import FrameBuilder

# Sorry about the name...
class FrameBuilderBuilder:
    @staticmethod
    def build() -> FrameBuilder:
        frame_list = FrameHelper.get_all_frames()
        inner_checker = InnerFrameChecker()
        frame_getter = FrameGetter(frame_list, inner_checker)
        frame_updater = UpdaterDictConstructor.build()
        frame_builder = FrameBuilder(frame_getter, frame_updater)
        return frame_builder

