from app.classes.selection.selected_node import SelectedNode
from app.classes.units.node_type import NodeType

# Final node needs to give initial value... e.g. date, CustomEvent, CommonEvent...
# TODO: May want to type/alias this
class FinalNode(SelectedNode[any]):
    node_type = NodeType.FINAL_NODE


