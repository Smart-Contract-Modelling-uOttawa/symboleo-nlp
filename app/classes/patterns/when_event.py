from app.classes.patterns.pattern import EventPattern
from app.classes.units.unit_type import UnitType

class WhenEvent(EventPattern):
    sequence = [UnitType.ROOT, UnitType.WHEN, UnitType.EVENT]
    
    def is_complete(self):
        return self.event.is_complete()

    def to_text(self):
        event_nl = f'{self.nl_event.to_text()}'
        return f'when {event_nl}'
    