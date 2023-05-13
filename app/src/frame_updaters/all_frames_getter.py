from typing import Type
from app.classes.frames.all_frames import *
from app.classes.frames.all_frames import Frame, List

class IGetAllFrames:
    def get(self) -> List[Frame]:
        raise NotImplementedError()

class AllFramesGetter(IGetAllFrames):
    def get(self) -> List[Frame]:
        return [
            BeforeEventFrame(),
            BeforeDateFrame(),
            WithinTimespanEventFrame(),
            IfEventFrame(),
            AfterDateFrame(),
            AfterEventFrame(),
            UntilEventFrame(),
            BeforeTimePointFrame(),
            UntilTimespanFrame()
        ]
