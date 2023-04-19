from app.classes.frames.frame import Frame
from app.classes.tokens.node_type import NodeType
from app.src.operations.refine_parameter2.parm_configs import ParmOpCode

class AfterEventFrame(Frame):
    pattern = [NodeType.ROOT, NodeType.AFTER, NodeType.EVENT]
    op_code = ParmOpCode.REFINE_PREDICATE
    event_text = ''
    
    def is_complete(self):
        return self.event_text != ''

    def to_text(self):
        event_nl = f'{self.event_text}'
        return f'after {event_nl}'
    