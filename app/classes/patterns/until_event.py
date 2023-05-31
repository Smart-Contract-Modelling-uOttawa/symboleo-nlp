from app.classes.patterns.pattern import EventPattern
from app.classes.units.unit_type import UnitType
from app.classes.custom_event.conj_type import ConjType
from app.src.operations.refine_parameter.parm_configs import ParmOpCode

class UntilEvent(EventPattern):
    sequence = [UnitType.ROOT, UnitType.UNTIL, UnitType.EVENT]
    op_code = ParmOpCode.REFINE_PREDICATE

    def is_complete(self):
        return self.event.is_complete() 

    def to_text(self):
        return f'until {self.event.to_text(ConjType.PRESENT)}'

