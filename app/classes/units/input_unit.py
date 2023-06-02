from __future__ import annotations
from typing import List, Type
from app.classes.elements.element import Element
from app.classes.units.unit_type import UnitType

class InputUnit: # pragma: no cover
    id: str = None
    unit_type: UnitType = None
    prompt: str = None
    children: List[Type[Element]] = []
    needs_value = False
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
