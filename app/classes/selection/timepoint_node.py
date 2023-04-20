from app.classes.selection.selected_node import SelectedNode
from app.classes.tokens.node_type import NodeType

class TimepointNode(SelectedNode[str]):
    node_type = NodeType.TIMEPOINT
