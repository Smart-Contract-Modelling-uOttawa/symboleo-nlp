from __future__ import annotations
from enum import Enum
from app.classes.spec.sym_point import PointExpression, PointAtom

class TimeUnit(Enum):
    Seconds = 'seconds'
    Minutes = 'minutes'
    Hours = 'hours'
    Days = 'days'
    Weeks = 'weeks'
    Months = 'months'
    Years = 'years'


class PointFunctionName(Enum):
    DateAdd = 'Date.add'

# Note: Changed the arg from PointExpression to PointAtom to avoid recursion
# This will disallow the existence of recursive pointFunctions (examples?)
class PointFunction(PointExpression):
    arg = PointAtom()
    
    def __init__(self, arg: PointAtom, time_value: int, time_unit: TimeUnit):
        self.name: PointFunctionName = PointFunctionName.DateAdd # Can make this an arg if this type expands
        self.arg = arg
        self.time_value = int(time_value)
        self.time_unit = time_unit

    def __eq__(self, other: PointFunction) -> bool:
        return self.arg == other.arg and self.time_unit == other.time_unit and self.time_value == other.time_value

    def to_sym(self):
        return f'{self.name.value}({self.arg.to_sym()}, {self.time_value}, {self.time_unit.value})'