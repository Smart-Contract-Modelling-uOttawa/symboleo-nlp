from app.classes.frames.frame import Frame
from app.classes.grammar.node_type import NodeType
from app.src.operations.configs import OpCode

# TODO: This will be updated to handle domain event timepoints
class BeforeTimePointFrame(Frame):
    pattern = [NodeType.ROOT, NodeType.BEFORE, NodeType.TIMEPOINT]
    op_code = OpCode.REFINE_PREDICATE
    timepoint: str = ''

    def is_complete(self):
        return self.timepoint != '' 

    def to_text(self):
        return f'before {self.timepoint}'
    