from __future__ import annotations
from typing import List
import copy

from app.classes.events.base_event import BaseEvent
from app.classes.events.custom_event.custom_event import CustomEvent
from app.classes.units.unit_type import UnitType

class Pattern: # pragma: no cover
    sequence: List[UnitType]

    def to_text(self) -> str:
        raise NotImplementedError()
    
    def is_complete(self) -> bool:
        return False
    
    @staticmethod
    def copy(pattern: Pattern):
        return copy.deepcopy(pattern)


class EventPattern(Pattern):
    def __init__(self) -> None:
        self.event = CustomEvent() # Need a place to set this to a specific type...
        self.nl_event = CustomEvent()


class DummyPattern(Pattern):
    sequence = [UnitType.ROOT]
    test_value: str = ''

    def is_complete(self):
        return self.test_value != '' 

    def to_text(self):
        return f'DUMMY: {self.test_value}'
    
    
