from app.src.frame_updaters.inner_frame_checker import InnerFrameChecker
from app.src.frame_updaters.frame_getter import FrameGetter
from app.src.frame_updaters.all_frames_getter import AllFramesGetter
from app.src.frame_updaters.frame_updater_dict import FrameUpdaterDictConstructor
from app.src.frame_updaters.frame_builder import FrameBuilder

# Sorry about the name...
class FrameBuilderBuilder:
    @staticmethod
    def build() -> FrameBuilder:
        all_frames_getter = AllFramesGetter()
        inner_checker = InnerFrameChecker()
        frame_getter = FrameGetter(all_frames_getter, inner_checker)
        frame_updater = FrameUpdaterDictConstructor.build()
        frame_builder = FrameBuilder(frame_getter, frame_updater)
        return frame_builder

