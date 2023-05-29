from app.classes.elements.element import Element
from app.classes.units.unit_type import UnitType

class RootElement(Element):
    unit_type = UnitType.ROOT

class AfterElement(Element):
    unit_type = UnitType.AFTER

class BeforeElement(Element):
    unit_type = UnitType.BEFORE

class IfElement(Element):
    unit_type = UnitType.IF

class UntilElement(Element):
    unit_type = UnitType.UNTIL

class WithinElement(Element):
    unit_type = UnitType.WITHIN

class ForElement(Element):
    unit_type = UnitType.FOR

class FollowingElement(Element):
    unit_type = UnitType.FOLLOWING

class UnlessElement(Element):
    unit_type = UnitType.UNLESS


# Final node needs to give initial value... e.g. date, CustomEvent, CommonEvent...
# TODO: May want to type/alias this
class FinalElement(Element[any]):
    unit_type = UnitType.FINAL_NODE

