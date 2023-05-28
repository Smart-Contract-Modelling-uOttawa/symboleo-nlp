
from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType


class TimepointUnit(InputUnit):
    unit_type = UnitType.TIMEPOINT
    prompt = 'Specify a timepoint'
    needs_value = True
