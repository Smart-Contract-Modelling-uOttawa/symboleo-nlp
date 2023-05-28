from app.classes.patterns.pattern import Pattern
from app.classes.units.unit_type import UnitType
from app.src.operations.refine_parameter.parm_configs import ParmOpCode

# Maybe date should be a subclass of Timepoint...?
class BeforeDate(Pattern):
    sequence = [UnitType.ROOT, UnitType.BEFORE, UnitType.DATE]
    op_code = ParmOpCode.REFINE_PREDICATE
    date_text: str = ''

    def is_complete(self):
        return self.date_text != ''

    def to_text(self):
        return f'before {self.date_text}'
