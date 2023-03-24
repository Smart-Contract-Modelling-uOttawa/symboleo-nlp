from app.classes.frames.frame import Frame
from app.classes.grammar.node_type import NodeType
from app.src.operations.parm_operations.parameter_updater import ParmOpCode

class BeforeTimePointFrame(Frame):
    pattern = [NodeType.ROOT, NodeType.BEFORE, NodeType.TIMEPOINT]
    op_code = ParmOpCode.REFINE_PREDICATE
    timepoint: str = ''

    def is_complete(self):
        return self.timepoint != '' 

    def to_text(self):
        return f'before {self.timepoint}'
    