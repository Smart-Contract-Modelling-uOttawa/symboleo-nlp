from app.classes.elements.element import Element
from app.classes.units.node_type import NodeType

class DateNode(Element[str]):
    node_type = NodeType.DATE