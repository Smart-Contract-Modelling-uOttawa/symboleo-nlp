from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

from app.classes.units.event_unit import EventUnit
from app.classes.units.date_unit import DateUnit
from app.classes.units.timepoint_unit import TimepointUnit

class BeforeUnit(InputUnit):
    unit_type = UnitType.BEFORE
    prompt = 'before'
    init_value = 'before'
    children = [EventUnit, DateUnit, TimepointUnit]

