from app.classes.frames.before_event_frame import \
    BeforeEventFrame, BeforeDateFrame, WithinTimespanEventFrame

from app.classes.frames.if_state_frame import IfStateFrame


def get_all_frames():
    return [
        BeforeEventFrame(),
        BeforeDateFrame(),
        WithinTimespanEventFrame(),
        IfStateFrame()
    ]