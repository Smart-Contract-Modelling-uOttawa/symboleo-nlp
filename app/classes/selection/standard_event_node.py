from app.classes.spec.sym_event import ObligationEventName, ContractEventName
from app.classes.template_event.common_event import CommonEvent
from app.classes.template_event.obligation_subject import ObligationSubject
from app.classes.selection.selected_node import SelectedNode
from app.classes.units.node_type import NodeType

class ObligationActionNode(SelectedNode[ObligationEventName]):
    node_type = NodeType.CONTRACT_ACTION

class ObligationSubjectNode(SelectedNode[ObligationSubject]):
    node_type = NodeType.CONTRACT_SUBJECT

class NormEventNode(SelectedNode):
    node_type = NodeType.CONTRACT_EVENT



class ContractActionNode(SelectedNode[ContractEventName]):
    node_type = NodeType.CONTRACT_ACTION

class ContractSubjectNode(SelectedNode): 
    node_type = NodeType.CONTRACT_SUBJECT

class ContractEventNode(SelectedNode):
    node_type = NodeType.CONTRACT_EVENT

class CommonEventNode(SelectedNode[CommonEvent]):
    node_type = NodeType.COMMON_EVENT

class StandardEventNode(SelectedNode):
    node_type = NodeType.STANDARD_EVENT

