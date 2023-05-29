from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

from app.classes.units.event_unit import EventUnit

class UnlessUnit(InputUnit):
    unit_type = UnitType.UNLESS
    prompt = 'Unless'
    init_value = 'unless'
    children = [EventUnit]