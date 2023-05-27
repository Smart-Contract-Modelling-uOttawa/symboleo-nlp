from app.classes.patterns.pattern import EventPattern
from app.classes.units.node_type import NodeType
from app.src.operations.refine_parameter.parm_configs import ParmOpCode

class BeforeTimePointFrame(EventPattern):
    pattern = [NodeType.ROOT, NodeType.BEFORE, NodeType.TIMEPOINT]
    op_code = ParmOpCode.REFINE_PREDICATE
    timepoint: str = ''

    def is_complete(self):
        return self.timepoint != '' 

    def to_text(self):
        return f'before {self.timepoint}'
    