from app.classes.frames.frame import Frame
from app.classes.grammar.node_type import NodeType
from app.src.operations.configs import OpCode

class WithinTimespanDateFrame(Frame):
    pattern = [NodeType.ROOT, NodeType.WITHIN, NodeType.TIMESPAN, NodeType.DATE]
    op_code = OpCode.REFINE_PREDICATE
    timespan: str = ''
    date_text: str = ''

    def is_complete(self):
        return self.timespan != '' and self.date_text != ''

    def to_text(self):
        return f'within {self.timespan} of {self.date_text}'

