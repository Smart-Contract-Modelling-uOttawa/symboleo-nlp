from app.classes.frames.before_event_frame import BeforeEventFrame, BeforeDateFrame, WithinTimespanEventFrame 

def get_all_frames():
    return [
        BeforeEventFrame(),
        BeforeDateFrame(),
        WithinTimespanEventFrame(),
        #...
    ]
