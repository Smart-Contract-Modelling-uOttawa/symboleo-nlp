from app.classes.units.unit_variety import UnitVariety
from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

class DateUnit(InputUnit):
    unit_type = UnitType.DATE
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Date'
    info = 'Enter a date (DD/MM/YYYY)'

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
    info = 'Choose/Enter a time unit'

class TimeValueUnit(InputUnit):
    unit_type = UnitType.TIME_VALUE
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Time value'
    info = 'Enter a time value (integer)'

class TimePeriodUnit(InputUnit):
    unit_type = UnitType.TIME_PERIOD
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Time period'
    info = 'Choose or enter a time period'
