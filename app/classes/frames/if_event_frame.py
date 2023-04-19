from app.classes.frames.frame import Frame
from app.classes.tokens.node_type import NodeType
from app.src.operations.refine_parameter2.parm_configs import ParmOpCode
from app.classes.other.frame_event import FrameEvent

class IfEventFrame(Frame):
    pattern = [NodeType.ROOT, NodeType.IF, NodeType.EVENT]
    op_code = ParmOpCode.ADD_TRIGGER
    frame_event: FrameEvent = FrameEvent()
    
    def is_complete(self):
        return self.frame_event.is_complete()

    # TODO: The NL will likely not be a string - will be a more complex NL object that can be conjugated as needed.
    def to_text(self):
        event_nl = f'{self.frame_event.to_text()}'
        return f'if {event_nl}'
    