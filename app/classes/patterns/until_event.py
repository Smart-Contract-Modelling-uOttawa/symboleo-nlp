from app.classes.patterns.pattern import EventPattern
from app.classes.units.unit_type import UnitType
from app.classes.events.conj_type import ConjType

class UntilEvent(EventPattern):
    sequence = [UnitType.ROOT, UnitType.UNTIL, UnitType.EVENT]

    def is_complete(self):
        return self.event.is_complete() 

    def to_text(self):
        return f'until {self.event.to_text(ConjType.PRESENT)}'

