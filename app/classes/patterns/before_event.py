
from app.classes.patterns.pattern import EventPattern
from app.classes.units.unit_type import UnitType

class BeforeEvent(EventPattern):
    sequence = [UnitType.ROOT, UnitType.BEFORE, UnitType.EVENT]

    def is_complete(self):
        return self.event.is_complete()

    def to_text(self):
        event_nl = f'{self.nl_event.to_text()}'
        return f'before {event_nl}'
    
