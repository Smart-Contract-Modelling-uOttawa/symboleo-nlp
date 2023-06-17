from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

from app.classes.units.custom_event_units import *

class FailsToUnit(InputUnit):
    unit_type = UnitType.FAILS_TO
    prompt = 'fails to'
    init_value = 'fails to'
    children = [TransitiveVerbUnit, IntransitiveVerbUnit, LinkingVerbUnit]