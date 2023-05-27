from app.classes.selection.selected_node import SelectedNode
from app.classes.custom_event.custom_event import CustomEvent
from app.classes.units.node_type import NodeType

class EventNode(SelectedNode):
    node_type = NodeType.EVENT
