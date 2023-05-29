from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

from app.classes.units.timespan_unit import TimespanUnit

class ForUnit(InputUnit):
    unit_type = UnitType.FOR
    prompt = 'For'
    init_value = 'for'
    children = [TimespanUnit]
