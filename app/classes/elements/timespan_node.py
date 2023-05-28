from app.classes.elements.element import Element
from app.classes.other.timespan import Timespan
from app.classes.units.unit_type import UnitType

class TimespanNode(Element[Timespan]):
    node_type = UnitType.TIMESPAN
