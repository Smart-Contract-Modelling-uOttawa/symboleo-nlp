from app.classes.spec.sym_event import ObligationEventName, ContractEventName
from app.classes.template_event.common_event import CommonEvent
from app.classes.template_event.obligation_subject import ObligationSubject
from app.classes.elements.element import Element
from app.classes.units.unit_type import UnitType

class ObligationActionNode(Element[ObligationEventName]):
    node_type = UnitType.CONTRACT_ACTION

class ObligationSubjectNode(Element[ObligationSubject]):
    node_type = UnitType.CONTRACT_SUBJECT

class NormEventNode(Element):
    node_type = UnitType.CONTRACT_EVENT



class ContractActionNode(Element[ContractEventName]):
    node_type = UnitType.CONTRACT_ACTION

class ContractSubjectNode(Element): 
    node_type = UnitType.CONTRACT_SUBJECT

class ContractEventNode(Element):
    node_type = UnitType.CONTRACT_EVENT

class CommonEventNode(Element[CommonEvent]):
    node_type = UnitType.COMMON_EVENT

class StandardEventNode(Element):
    node_type = UnitType.STANDARD_EVENT

