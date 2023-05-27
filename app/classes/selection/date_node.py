from app.classes.selection.selected_node import SelectedNode
from app.classes.units.node_type import NodeType

class DateNode(SelectedNode[str]):
    node_type = NodeType.DATE