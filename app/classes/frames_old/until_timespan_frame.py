from app.classes.patterns.pattern import EventPattern
from app.classes.units.unit_type import UnitType
from app.src.operations.refine_parameter.parm_configs import ParmOpCode
from app.classes.custom_event.conj_type import ConjType

# TODO: Will be a bit of a special case
## e.g. for "situation"-like events that are negated
class UntilTimespanFrame(EventPattern):
    pattern = [UnitType.ROOT, UnitType.UNTIL, UnitType.TIMESPAN]
    op_code = ParmOpCode.REFINE_PREDICATE

    def __init__(self) -> None:
        super().__init__()
        self.prep = None
        self.timespan = None
    
    def is_complete(self):
        return self.event.is_complete()

    def to_text(self):
        return f'until {self.timespan} {self.prep} {self.event.to_text(ConjType.CONTINUOUS)}'
