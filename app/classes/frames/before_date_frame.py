from app.classes.frames.frame import Frame
from app.classes.grammar.node_type import NodeType
from app.src.operations.configs import OpCode

# Maybe date should be a subclass of Timepoint...?
class BeforeDateFrame(Frame):
    pattern = [NodeType.ROOT, NodeType.BEFORE, NodeType.DATE]
    op_code = OpCode.REFINE_PREDICATE
    date_text: str = ''

    def is_complete(self):
        return self.date_text != ''

    def to_text(self):
        return f'before {self.date_text}'
