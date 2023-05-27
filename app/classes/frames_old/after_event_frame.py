from app.classes.patterns.pattern import Pattern, EventPattern
from app.classes.tokens.node_type import NodeType
from app.src.operations.refine_parameter.parm_configs import ParmOpCode

class AfterEventPattern(EventPattern):
    pattern = [NodeType.ROOT, NodeType.AFTER, NodeType.EVENT]
    op_code = ParmOpCode.REFINE_PREDICATE
    
    def is_complete(self):
        return self.event.is_complete()

    def to_text(self):
        event_nl = f'{self.event.to_text()}'
        return f'after {event_nl}'
    