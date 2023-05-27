from app.classes.patterns.pattern import EventPattern
from app.classes.units.node_type import NodeType
from app.src.operations.refine_parameter.parm_configs import ParmOpCode

class BeforeEvent(EventPattern):
    sequence = [NodeType.ROOT, NodeType.BEFORE, NodeType.EVENT]
    op_code = ParmOpCode.REFINE_PREDICATE
    
    def is_complete(self):
        return self.event.is_complete()

    def to_text(self):
        event_nl = f'{self.event.to_text()}'
        return f'before {event_nl}'
    
