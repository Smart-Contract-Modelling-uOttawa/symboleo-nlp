from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

from app.classes.units.event_unit import EventUnit

class OfUnit(InputUnit):
    unit_type = UnitType.OF
    prompt = 'Of'
    init_value = 'of'
    children = [EventUnit]
