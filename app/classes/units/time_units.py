from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

class DateUnit(InputUnit):
    unit_type = UnitType.DATE
    prompt = 'Enter a date'
    needs_value = True

class EventUnit(InputUnit):
    unit_type = UnitType.EVENT
    prompt = 'Describe an event'

# TODO: ?
class TimepointUnit(InputUnit):
    unit_type = UnitType.TIMEPOINT
    prompt = 'Specify a timepoint'
    needs_value = True

class TimespanUnit(InputUnit):
    unit_type = UnitType.TIMESPAN
    prompt = 'Enter a timespan'
    needs_value = True