from app.classes.spec.sym_event import ObligationEventName, ContractEventName
from app.classes.template_event.common_event import CommonEvent
from app.classes.template_event.obligation_subject import ObligationSubject
from app.classes.elements.element import Element
from app.classes.units.node_type import NodeType

class ObligationActionNode(Element[ObligationEventName]):
    node_type = NodeType.CONTRACT_ACTION

class ObligationSubjectNode(Element[ObligationSubject]):
    node_type = NodeType.CONTRACT_SUBJECT

class NormEventNode(Element):
    node_type = NodeType.CONTRACT_EVENT



class ContractActionNode(Element[ContractEventName]):
    node_type = NodeType.CONTRACT_ACTION

class ContractSubjectNode(Element): 
    node_type = NodeType.CONTRACT_SUBJECT

class ContractEventNode(Element):
    node_type = NodeType.CONTRACT_EVENT

class CommonEventNode(Element[CommonEvent]):
    node_type = NodeType.COMMON_EVENT

class StandardEventNode(Element):
    node_type = NodeType.STANDARD_EVENT

