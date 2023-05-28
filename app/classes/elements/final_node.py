from app.classes.elements.element import Element
from app.classes.units.unit_type import UnitType

# Final node needs to give initial value... e.g. date, CustomEvent, CommonEvent...
# TODO: May want to type/alias this
class FinalNode(Element[any]):
    node_type = UnitType.FINAL_NODE


