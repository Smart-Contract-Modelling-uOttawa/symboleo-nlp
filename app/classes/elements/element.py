from __future__ import annotations
from typing import TypeVar, Generic
from app.classes.units.unit_type import UnitType

T = TypeVar('T')

class Element(Generic[T]):
    unit_type: UnitType = None

    def __init__(self, value: T = None, input_value:str = None):
        self.value = value
        self.input_value = input_value

class DummyElement(Element):
    unit_type = UnitType.DUMMY
