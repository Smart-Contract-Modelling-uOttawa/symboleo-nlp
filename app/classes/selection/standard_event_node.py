from app.classes.spec.sym_event import ContractEventName
from app.classes.selection.selected_node import SelectedNode
from app.classes.tokens.node_type import NodeType

class ContractActionNode(SelectedNode[ContractEventName]):
    node_type = NodeType.CONTRACT_ACTION

class ContractSubjectNode(SelectedNode): # Shouldnt need a value. always just "contract"
    node_type = NodeType.CONTRACT_SUBJECT

class ContractEventNode(SelectedNode):
    node_type = NodeType.CONTRACT_EVENT

class StandardEventNode(SelectedNode):
    node_type = NodeType.STANDARD_EVENT

