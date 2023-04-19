from app.classes.selection.selected_node import SelectedNode
from app.classes.tokens.node_type import NodeType

class IfNode(SelectedNode):
    node_type = NodeType.IF
    prompt = 'If'
