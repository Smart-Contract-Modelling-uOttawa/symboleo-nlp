from app.classes.patterns.pattern import EventPattern
from app.classes.units.unit_type import UnitType
from app.classes.events.conj_type import ConjType

class UnlessEvent(EventPattern):
    sequence = [UnitType.ROOT, UnitType.UNLESS, UnitType.EVENT]

    def is_complete(self):
        return self.event.is_complete() 

    def to_text(self):
        return f'unless {self.nl_event.to_text()}'

