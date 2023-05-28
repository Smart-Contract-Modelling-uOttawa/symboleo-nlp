from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

from app.classes.units.timespan_unit import TimespanUnit

class WithinUnit(InputUnit):
    unit_type = UnitType.WITHIN
    prompt = 'Within'
    init_value = 'within'
    children = [TimespanUnit]