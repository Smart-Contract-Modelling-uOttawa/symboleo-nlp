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

class WhenElement(Element):
    unit_type = UnitType.WHEN

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

class OfElement(Element):
    unit_type = UnitType.OF


# TODO: E2 - Should strongly type/alias this
## And figure out what its purpose is 
class FinalElement(Element[any]):
    unit_type = UnitType.FINAL_NODE

