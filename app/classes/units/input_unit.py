from __future__ import annotations
from typing import List
from app.classes.units.unit_type import UnitType, UnitVariety

class InputUnit: # pragma: no cover
    unit_type: UnitType = None
    prompt: str = None
    unit_var: UnitVariety = UnitVariety.STATIC
    needs_value = False # Should change this to unit_func (static, dynamic, empty)
    init_value = ''
    options: List[str] = None
    
    def __init__(self, options: List[str] = None):
        self.options = options 
    
    def __eq__(self, other: InputUnit) -> bool:
        return self.unit_type == other.unit_type

    def get_value(self):
        raise NotImplementedError()


class DummyUnit(InputUnit):
    prompt = 'dummy'
    unit_type = UnitType.DUMMY
