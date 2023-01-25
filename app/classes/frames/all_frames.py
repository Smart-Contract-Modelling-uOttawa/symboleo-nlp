from app.classes.frames.before_event_frame import \
    BeforeEventFrame, BeforeDateFrame, WithinTimespanEventFrame

from app.classes.frames.if_state_frame import IfStateFrame

# Question: Will I need to fetch different frames depending on the parameter type that I am filling?
## I think so...
## Then we'll need to inject them as the "possible frames" on the selection object...
## Will probably need a better way to organize this..

def get_pp_frames():
    return [
        BeforeEventFrame(),
        BeforeDateFrame(),
        WithinTimespanEventFrame(),
        #...
    ]

def get_cond_frames():
    return [
        IfStateFrame()
    ]

# Frames to add - some of these may be synonyms... do we want to include them
## Upon contract termination: 
## When contract has been terminated