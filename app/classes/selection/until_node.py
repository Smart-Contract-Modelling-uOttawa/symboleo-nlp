from app.classes.selection.selected_node import SelectedNode
from app.classes.tokens.node_type import NodeType

# Will likely change this to "unless"
class UntilNode(SelectedNode):
    node_type = NodeType.UNTIL
    prompt = 'Until'
