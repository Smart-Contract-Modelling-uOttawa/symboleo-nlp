from app.classes.patterns.pattern import EventPattern
from app.classes.elements.timespan import Timespan
from app.classes.units.unit_type import UnitType
from app.classes.events.conj_type import ConjType

class ForTimespanFollowingEvent(EventPattern):
    sequence = [UnitType.ROOT, UnitType.FOR, UnitType.TIMESPAN, UnitType.FOLLOWING, UnitType.EVENT]
    timespan: Timespan

    def is_complete(self):
        return self.event.is_complete() and self.timespan 

    def to_text(self):
        return f'for {self.timespan.to_text()} following {self.nl_event.to_text(ConjType.CONTINUOUS)}'

