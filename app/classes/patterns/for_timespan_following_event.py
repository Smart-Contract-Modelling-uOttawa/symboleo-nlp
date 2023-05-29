from app.classes.patterns.pattern import EventPattern
from app.classes.other.timespan import Timespan
from app.classes.units.unit_type import UnitType
from app.classes.custom_event.conj_type import ConjType
from app.src.operations.refine_parameter.parm_configs import ParmOpCode

class ForTimespanFollowingEvent(EventPattern):
    sequence = [UnitType.ROOT, UnitType.FOR, UnitType.TIMESPAN, UnitType.FOLLOWING, UnitType.EVENT]
    op_code = ParmOpCode.REFINE_PREDICATE
    timespan: Timespan

    def is_complete(self):
        return self.event.is_complete() and self.timespan 

    def to_text(self):
        return f'for {self.timespan.to_text()} following {self.event.to_text(ConjType.CONTINUOUS)}'

