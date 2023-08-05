from __future__ import annotations
from typing import List
import json
from app.classes.units.unit_type import UnitType, UnitVariety

class InputUnit: # pragma: no cover
    unit_type: UnitType = None
    prompt: str = None
    unit_var: UnitVariety = UnitVariety.STATIC
    info: str = None
    init_value: str = None
    options: List[str] = None
    
    def __init__(self, options: List[str] = None):
        self.options = options 
    
    def __eq__(self, other: InputUnit) -> bool:
        return self.unit_type == other.unit_type

    def get_value(self):
        raise NotImplementedError()
    
    def to_dict(self):
        return {
            'options': self.options,
            'prompt': self.prompt,
            'variety': str(self.unit_var),
            'unit_type': str(self.unit_type.name),
            'default_value': self.init_value,
            'info': self.info
        }


class DummyUnit(InputUnit):
    prompt = 'dummy'
    unit_type = UnitType.DUMMY
