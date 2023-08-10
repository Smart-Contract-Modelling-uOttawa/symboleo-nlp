from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType, UnitVariety

class DateUnit(InputUnit):
    unit_type = UnitType.DATE
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Date'

class EventUnit(InputUnit):
    unit_type = UnitType.EVENT
    unit_var = UnitVariety.EMPTY
    prompt = 'Event'


class TimespanUnit(InputUnit):
    unit_type = UnitType.TIMESPAN
    prompt = 'Timespan'
    unit_var = UnitVariety.EMPTY

class TimeUnitUnit(InputUnit):
    unit_type = UnitType.TIME_UNIT
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Time unit'

class TimeValueUnit(InputUnit):
    unit_type = UnitType.TIME_VALUE
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Time value'

class TimePeriodUnit(InputUnit):
    unit_type = UnitType.TIME_PERIOD
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Time period'
