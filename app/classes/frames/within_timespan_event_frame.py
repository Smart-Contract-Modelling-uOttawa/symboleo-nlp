from app.classes.frames.frame import Frame
from app.classes.tokens.node_type import NodeType
from app.src.operations.parm_configs import ParmOpCode

class WithinTimespanEventFrame(Frame):
    pattern = [NodeType.ROOT, NodeType.WITHIN, NodeType.TIMESPAN, NodeType.EVENT]
    op_code = ParmOpCode.REFINE_PREDICATE
    timespan: str = ''
    subject: str = ''
    verb: str = ''

    def is_complete(self):
        return self.subject != '' and self.verb != '' and self.timespan != ''

    def to_text(self):
        return f'within {self.timespan} of {self.subject} being {self.verb}'

