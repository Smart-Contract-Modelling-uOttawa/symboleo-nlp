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
    DateAdd = 'Date.Add'

# Note: Changed the arg from PointExpression to PointAtom to avoid recursion
# This will disallow the existence of recursive pointFunctions (examples?)
class PointFunction(PointExpression):
    arg = PointAtom()
    # value: int = 0
    # unit: TimeUnit = None
    
    def __init__(self, arg: PointAtom, value: int, time_unit: TimeUnit):
        self.name: PointFunctionName = PointFunctionName.DateAdd # Can make this an arg if this type expands
        self.arg = arg
        self.value = value
        self.time_unit = time_unit

    def to_sym(self):
        return f'{self.name.value}({self.arg.to_sym()}, {self.value}, {self.time_unit.value})'