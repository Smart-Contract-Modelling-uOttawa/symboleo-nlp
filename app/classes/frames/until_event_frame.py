from app.classes.frames.frame import Frame
from app.classes.tokens.node_type import NodeType
from app.src.operations.refine_parameter2.parm_configs import ParmOpCode
from app.classes.other.frame_event import FrameEvent

# TODO: Will likely be replaced by "Unless"
class UntilEventFrame(Frame):
    pattern = [NodeType.ROOT, NodeType.UNTIL, NodeType.EVENT]
    op_code = ParmOpCode.ADD_NORM
    frame_event = FrameEvent()
    
    def is_complete(self):
        return self.frame_event.is_complete()

    def to_text(self):
        event_nl = f'{self.frame_event.to_text()}'
        return f'until {event_nl}'
