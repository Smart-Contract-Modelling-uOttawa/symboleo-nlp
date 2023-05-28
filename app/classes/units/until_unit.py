from typing import List
from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

from app.classes.units.event_unit import EventUnit

class UntilUnit(InputUnit):
    unit_type = UnitType.UNTIL
    prompt = 'Until'
    init_value = 'until'
    children = [EventUnit]