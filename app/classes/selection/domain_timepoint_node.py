from app.classes.selection.selected_node import SelectedNode
from app.classes.tokens.node_type import NodeType

class DomainTimepointNode(SelectedNode[str]):
    node_type = NodeType.DOMAIN_TIMEPOINT

