from app.classes.selection.selected_node import SelectedNode
from app.classes.tokens.node_type import NodeType

class StandardEventNode(SelectedNode):
    node_type = NodeType.STANDARD_EVENT
    prompt = 'Standard Event'

