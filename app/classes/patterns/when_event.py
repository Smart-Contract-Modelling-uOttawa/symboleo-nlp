from app.classes.patterns.pattern import EventPattern
from app.classes.units.unit_type import UnitType
from app.src.operations.refine_parameter.parm_configs import ParmOpCode

class WhenEvent(EventPattern):
    sequence = [UnitType.ROOT, UnitType.WHEN, UnitType.EVENT]
    op_code = ParmOpCode.ADD_TRIGGER
    
    def is_complete(self):
        return self.event.is_complete()

    def to_text(self):
        event_nl = f'{self.event.to_text()}'
        return f'when {event_nl}'
    