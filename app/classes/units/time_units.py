from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType, UnitVariety

class DateUnit(InputUnit):
    unit_type = UnitType.DATE
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Enter a date'
    needs_value = True

class EventUnit(InputUnit):
    unit_type = UnitType.EVENT
    unit_var = UnitVariety.EMPTY
    prompt = 'Describe an event'

# TODO: Keeping this?
class TimepointUnit(InputUnit):
    unit_type = UnitType.TIMEPOINT
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Specify a timepoint'
    needs_value = True

class TimespanUnit(InputUnit):
    unit_type = UnitType.TIMESPAN
    unit_var = UnitVariety.EMPTY

class TimeUnitUnit(InputUnit):
    unit_type = UnitType.TIME_UNIT
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Enter a time unit'
    needs_value = True

class TimeValueUnit(InputUnit):
    unit_type = UnitType.TIME_VALUE
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Enter a time value (int)'
    needs_value = True

class TimePeriodUnit(InputUnit):
    unit_type = UnitType.TIME_PERIOD
    unit_var = UnitVariety.DYNAMIC
    prompt = 'Enter a time period'
    needs_value = True
