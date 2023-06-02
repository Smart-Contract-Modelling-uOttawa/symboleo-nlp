from app.classes.patterns.pattern import Pattern
from app.classes.units.unit_type import UnitType

class BeforeDate(Pattern):
    sequence = [UnitType.ROOT, UnitType.BEFORE, UnitType.DATE]
    date_text: str = ''

    def is_complete(self):
        return self.date_text != ''

    def to_text(self):
        return f'before {self.date_text}'
