from typing import List
from app.classes.frames.frame import Frame
from app.classes.frames.before_event_frame import BeforeEventFrame
from app.classes.frames.before_date_frame import BeforeDateFrame
from app.classes.frames.after_event_frame import AfterEventFrame
from app.classes.frames.after_date_frame import AfterDateFrame
from app.classes.frames.within_timespan_event_frame import WithinTimespanEventFrame 
from app.classes.frames.if_event_frame import IfEventFrame
from app.classes.frames.until_event_frame import UntilEventFrame
from app.classes.frames.before_timepoint_frame import BeforeTimePointFrame

# TODO: Make these helper functions

# Maybe a helper...
def is_event_frame(frame: Frame) -> bool:
    return isinstance(frame, BeforeEventFrame) or \
        isinstance(frame, AfterEventFrame) or \
        isinstance(frame, WithinTimespanEventFrame) or \
        isinstance(frame, IfEventFrame) or \
        isinstance(frame, UntilEventFrame)


def get_all_frames() -> List[Frame]:
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