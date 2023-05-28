from app.classes.elements.element import Element
from app.classes.units.node_type import NodeType

class DomainTimepointNode(Element[str]):
    node_type = NodeType.DOMAIN_TIMEPOINT

