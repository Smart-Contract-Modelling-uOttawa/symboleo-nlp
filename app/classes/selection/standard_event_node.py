from app.classes.spec.sym_event import ObligationEventName, ContractEventName
from app.classes.template_event.obligation_subject import ObligationSubject
from app.classes.selection.selected_node import SelectedNode
from app.classes.tokens.node_type import NodeType

class ObligationActionNode(SelectedNode[ObligationEventName]):
    node_type = NodeType.CONTRACT_ACTION

class ObligationSubjectNode(SelectedNode[ObligationSubject]):
    node_type = NodeType.CONTRACT_SUBJECT

class NormEventNode(SelectedNode):
    node_type = NodeType.CONTRACT_EVENT



class ContractActionNode(SelectedNode[ContractEventName]):
    node_type = NodeType.CONTRACT_ACTION

class ContractSubjectNode(SelectedNode): # Shouldnt need a value. always just "contract"
    node_type = NodeType.CONTRACT_SUBJECT

class ContractEventNode(SelectedNode):
    node_type = NodeType.CONTRACT_EVENT

class StandardEventNode(SelectedNode):
    node_type = NodeType.STANDARD_EVENT

