from app.src.frames.inner_frame_checker import InnerFrameChecker
from app.src.frames.frame_getter import FrameGetter
from app.classes.frames.all_frames import get_all_frames
from app.src.frame_updaters.updater_dict import UpdaterDictConstructor
from app.src.frames.frame_builder import FrameBuilder

class FrameBuilderBuilder:
    @staticmethod
    def build() -> FrameBuilder:
        frame_list = get_all_frames()
        inner_checker = InnerFrameChecker()
        frame_getter = FrameGetter(frame_list, inner_checker)
        frame_updater = UpdaterDictConstructor.build()
        frame_builder = FrameBuilder(frame_getter, frame_updater)
        return frame_builder

