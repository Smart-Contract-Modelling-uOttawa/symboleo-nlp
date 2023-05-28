from __future__ import annotations
from typing import List, Type
from app.classes.elements.element import Element
from app.classes.units.unit_type import UnitType

class InputUnit: # pragma: no cover
    id: str = None
    sn_type: Type[Element] = Element # Might be able to remove this
    node_type: UnitType = None
    prompt: str = None
    children: List[Type[Element]] = []
    needs_value = False
    init_value = ''
    options: List[str] = None
    # TODO: options...
    
    def __init__(self, options: List[str] = None):
        self.options = options 
    
    def __eq__(self, other: InputUnit) -> bool:
        return self.node_type == other.node_type # more here?

    def get_value(self):
        raise NotImplementedError()
    

class DummyNode(InputUnit):
    prompt = 'dummy'
    node_type = UnitType.DUMMY
