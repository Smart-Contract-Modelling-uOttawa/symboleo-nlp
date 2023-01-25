from app.classes.frames.before_event_frame import \
    BeforeEventFrame, BeforeDateFrame, WithinTimespanEventFrame

def get_all_frames():
    return [
        BeforeEventFrame(),
        BeforeDateFrame(),
        WithinTimespanEventFrame(),
        #...
    ]

# Frames to add - some of these may be synonyms... do we want to include them
## Upon contract termination: 
## When contract has been terminated