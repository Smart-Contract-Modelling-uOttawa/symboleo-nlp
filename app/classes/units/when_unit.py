from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

from app.classes.units.event_unit import EventUnit

class WhenUnit(InputUnit):
    unit_type = UnitType.WHEN
    prompt = 'When'
    init_value = 'when'
    children = [EventUnit]
