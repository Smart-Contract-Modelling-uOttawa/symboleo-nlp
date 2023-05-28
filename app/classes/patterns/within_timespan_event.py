from app.classes.patterns.pattern import EventPattern
from app.classes.other.timespan import Timespan
from app.classes.units.unit_type import UnitType
from app.classes.custom_event.conj_type import ConjType
from app.src.operations.refine_parameter.parm_configs import ParmOpCode

class WithinTimespanEvent(EventPattern):
    sequence = [UnitType.ROOT, UnitType.WITHIN, UnitType.TIMESPAN, UnitType.EVENT]
    op_code = ParmOpCode.REFINE_PREDICATE
    timespan: Timespan

    def is_complete(self):
        return self.event.is_complete() and self.timespan 

    def to_text(self):
        return f'within {self.timespan.to_text()} of {self.event.to_text(ConjType.CONTINUOUS)}'

