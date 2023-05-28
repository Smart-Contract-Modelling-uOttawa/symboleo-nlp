from app.classes.elements.element import Element
from app.classes.other.timespan import Timespan
from app.classes.units.node_type import NodeType

class TimespanNode(Element[Timespan]):
    node_type = NodeType.TIMESPAN
