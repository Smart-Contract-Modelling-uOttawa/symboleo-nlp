from typing import List
from app.classes.frames.frame import Frame
from app.classes.frames.before_event_frame import BeforeEventFrame
from app.classes.frames.before_date_frame import BeforeDateFrame
from app.classes.frames.within_timespan_event_frame import WithinTimespanEventFrame 
from app.classes.frames.if_event_frame import IfEventFrame


def get_all_frames() -> List[Frame]:
    return [
        BeforeEventFrame(),
        BeforeDateFrame(),
        WithinTimespanEventFrame(),
        IfEventFrame()
    ]