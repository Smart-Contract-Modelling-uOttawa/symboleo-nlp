from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

from app.classes.units.standard_event_units import NormEventUnit
from app.classes.units.custom_event_units import CustomEventUnit

class EventUnit(InputUnit):
    unit_type = UnitType.EVENT
    prompt = 'Describe an event'
    children = [NormEventUnit, CustomEventUnit]