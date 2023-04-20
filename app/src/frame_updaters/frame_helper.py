from app.classes.frames.all_frames import *

class FrameHelper:

    @staticmethod
    def get_all_frames():
        return [
            BeforeEventFrame(),
            BeforeDateFrame(),
            WithinTimespanEventFrame(),
            IfEventFrame(),
            AfterDateFrame(),
            AfterEventFrame(),
            UntilEventFrame(),
            BeforeTimePointFrame()
        ]
