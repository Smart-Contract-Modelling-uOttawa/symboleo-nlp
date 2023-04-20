from app.classes.selection.selected_node import SelectedNode
from app.classes.tokens.node_type import NodeType

from app.classes.other.subject import Subject

class ContractSubjectNode(SelectedNode[Subject]):
    node_type = NodeType.CONTRACT_SUBJECT

