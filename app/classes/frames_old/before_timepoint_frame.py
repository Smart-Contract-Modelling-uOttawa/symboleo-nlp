from app.classes.patterns.pattern import EventPattern
from app.classes.units.unit_type import UnitType
from app.src.operations.refine_parameter.parm_configs import ParmOpCode

class BeforeTimePointFrame(EventPattern):
    pattern = [UnitType.ROOT, UnitType.BEFORE, UnitType.TIMEPOINT]
    op_code = ParmOpCode.REFINE_PREDICATE
    timepoint: str = ''

    def is_complete(self):
        return self.timepoint != '' 

    def to_text(self):
        return f'before {self.timepoint}'
    