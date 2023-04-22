from app.classes.selection.selected_node import SelectedNode
from app.classes.tokens.node_type import NodeType

from app.classes.custom_event.verb import Verb

class ContractActionNode(SelectedNode[Verb]):
    node_type = NodeType.CONTRACT_ACTION
