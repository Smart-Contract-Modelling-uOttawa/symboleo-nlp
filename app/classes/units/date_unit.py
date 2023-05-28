from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

class DateUnit(InputUnit):
    unit_type = UnitType.DATE
    prompt = 'Enter a date'
    needs_value = True
