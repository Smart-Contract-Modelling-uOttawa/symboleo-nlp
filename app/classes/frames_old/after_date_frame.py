from app.classes.patterns.pattern import Pattern
from app.classes.tokens.node_type import NodeType
from app.src.operations.refine_parameter.parm_configs import ParmOpCode

class AfterDateFrame(Pattern):
    pattern = [NodeType.ROOT, NodeType.AFTER, NodeType.DATE]
    op_code = ParmOpCode.REFINE_PREDICATE
    date_text: str = ''

    def is_complete(self):
        return self.date_text != ''

    def to_text(self):
        return f'after {self.date_text}'
