from app.classes.spec.sym_event import ObligationEventName, ContractEventName
from app.classes.elements.obligation_subject import ObligationSubject
from app.classes.elements.element import Element
from app.classes.units.unit_type import UnitType

class ObligationActionElement(Element[ObligationEventName]):
    unit_type = UnitType.CONTRACT_ACTION

class ObligationSubjectElement(Element[ObligationSubject]):
    unit_type = UnitType.CONTRACT_SUBJECT

class NormEventElement(Element):
    unit_type = UnitType.CONTRACT_EVENT



class ContractActionElement(Element[ContractEventName]):
    unit_type = UnitType.CONTRACT_ACTION

class ContractSubjectElement(Element): 
    unit_type = UnitType.CONTRACT_SUBJECT

class ContractEventElement(Element):
    unit_type = UnitType.CONTRACT_EVENT

class StandardEventElement(Element):
    unit_type = UnitType.STANDARD_EVENT

