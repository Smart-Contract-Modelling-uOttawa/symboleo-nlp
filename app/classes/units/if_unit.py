from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

from app.classes.units.event_unit import EventUnit

class IfUnit(InputUnit):
    unit_type = UnitType.IF
    prompt = 'If'
    init_value = 'if'
    children = [EventUnit]
