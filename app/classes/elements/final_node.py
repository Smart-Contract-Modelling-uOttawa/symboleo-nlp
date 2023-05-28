from app.classes.elements.element import Element
from app.classes.units.node_type import NodeType

# Final node needs to give initial value... e.g. date, CustomEvent, CommonEvent...
# TODO: May want to type/alias this
class FinalNode(Element[any]):
    node_type = NodeType.FINAL_NODE


