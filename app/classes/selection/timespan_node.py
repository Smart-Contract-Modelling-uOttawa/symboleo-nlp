from app.classes.selection.selected_node import SelectedNode
from app.classes.other.timespan import Timespan
from app.classes.tokens.node_type import NodeType

class TimespanNode(SelectedNode[Timespan]):
    node_type = NodeType.TIMESPAN
