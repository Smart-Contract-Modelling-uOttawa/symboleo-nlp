from app.classes.frames.frame import Frame, EventFrame
from app.classes.tokens.node_type import NodeType
from app.src.operations.refine_parameter2.parm_configs import ParmOpCode
from app.classes.other.frame_event import ConjType

class WithinTimespanEventFrame(EventFrame):
    pattern = [NodeType.ROOT, NodeType.WITHIN, NodeType.TIMESPAN, NodeType.EVENT]
    op_code = ParmOpCode.REFINE_PREDICATE
    timespan: str = ''

    def is_complete(self):
        return self.frame_event.is_complete() and self.timespan != ''

    def to_text(self):
        return f'within {self.timespan} of {self.frame_event.to_text(ConjType.CONTINUOUS)}'

