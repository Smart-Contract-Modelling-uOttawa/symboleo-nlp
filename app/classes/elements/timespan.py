from __future__ import annotations
from app.classes.spec.point_function import TimeUnit

class Timespan:
    def __init__(self, time_value: int, time_unit: TimeUnit):
        self.time_unit = time_unit
        self.time_value = time_value
    
    def __eq__(self, other: Timespan) -> bool:
        return self.time_unit == other.time_unit and self.time_value == other.time_value

    def to_text(self) -> str:
        return f'{self.time_value} {self.time_unit}'