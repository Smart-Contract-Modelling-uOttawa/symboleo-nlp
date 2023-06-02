from app.classes.patterns.pattern import EventPattern
from app.classes.elements.timespan import Timespan
from app.classes.units.unit_type import UnitType
from app.classes.events.conj_type import ConjType

class WithinTimespanEvent(EventPattern):
    sequence = [UnitType.ROOT, UnitType.WITHIN, UnitType.TIMESPAN, UnitType.EVENT]
    timespan: Timespan

    def is_complete(self):
        return self.event.is_complete() and self.timespan 

    def to_text(self):
        return f'within {self.timespan.to_text()} of {self.event.to_text(ConjType.CONTINUOUS)}'

