from __future__ import annotations
from typing import List
import copy

from app.classes.custom_event.base_event import BaseEvent
from app.classes.custom_event.custom_event import CustomEvent
from app.classes.units.unit_type import UnitType
from app.src.operations.refine_parameter.parm_configs import ParmOpCode

class Pattern: # pragma: no cover
    sequence: List[UnitType]
    op_code: ParmOpCode # TODO: May be able to remove this

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
        # Could have both an NL event and a sym event thing on here...


class DummyPattern(Pattern):
    sequence = [UnitType.ROOT]
    op_code = ParmOpCode.REFINE_PREDICATE
    test_value: str = ''

    def is_complete(self):
        return self.test_value != '' 

    def to_text(self):
        return f'DUMMY: {self.test_value}'
    
    
