from __future__ import annotations
from typing import TypeVar, Generic
from app.classes.units.unit_type import UnitType

T = TypeVar('T')

class Element(Generic[T]): # pragma: no cover
    node_type: UnitType = None

    def __init__(self, value: T = None):
        self.value = value

class DummyNode(Element):
    node_type = UnitType.DUMMY
