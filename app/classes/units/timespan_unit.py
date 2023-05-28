
from typing import List
from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

from app.classes.units.event_unit import EventUnit

class TimespanUnit(InputUnit):
    unit_type = UnitType.TIMESPAN
    prompt = 'Enter a timespan'
    needs_value = True
    children = [EventUnit]
