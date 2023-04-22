from app.classes.selection.selected_node import SelectedNode
from app.classes.tokens.node_type import NodeType

# TODO: Will likely change this to "unless"
class UntilNode(SelectedNode):
    node_type = NodeType.UNTIL
