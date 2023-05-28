from app.classes.elements.element import Element
from app.classes.units.node_type import NodeType

class TimepointNode(Element[str]):
    node_type = NodeType.TIMEPOINT
