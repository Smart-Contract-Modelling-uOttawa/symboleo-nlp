from app.src.frame_updaters.inner_frame_checker import InnerFrameChecker
from app.src.frame_updaters.frame_getter import FrameGetter
from app.src.frame_updaters.frame_helper import FrameHelper
from app.src.frame_updaters.frame_updater_dict import FrameUpdaterDictConstructor
from app.src.frame_updaters.frame_builder import FrameBuilder

# Sorry about the name...
class FrameBuilderBuilder:
    @staticmethod
    def build() -> FrameBuilder:
        frame_list = FrameHelper.get_all_frames()
        inner_checker = InnerFrameChecker()
        frame_getter = FrameGetter(frame_list, inner_checker)
        frame_updater = FrameUpdaterDictConstructor.build()
        frame_builder = FrameBuilder(frame_getter, frame_updater)
        return frame_builder

