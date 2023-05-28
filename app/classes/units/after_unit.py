from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

from app.classes.units.event_unit import EventUnit
from app.classes.units.date_unit import DateUnit
from app.classes.units.timepoint_unit import TimepointUnit

class AfterUnit(InputUnit):
    unit_type = UnitType.AFTER
    prompt = 'after'
    init_value = 'after'
    children = [EventUnit, DateUnit, TimepointUnit]