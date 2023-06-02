from app.classes.elements.element import Element
from app.classes.units.unit_type import UnitType

# TODO: E1 - Merge all event elements into one file
class EventElement(Element):
    unit_type = UnitType.EVENT
