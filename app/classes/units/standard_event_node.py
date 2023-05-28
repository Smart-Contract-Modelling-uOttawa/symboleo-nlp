from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType
from app.classes.units.custom_event_node import SubjectNode

class ObligationActionNode(InputUnit):
    node_type = UnitType.OBLIGATION_ACTION
    prompt = 'Obligation Action'
    needs_value = True

class ObligationSubjectNode(InputUnit):
    node_type = UnitType.OBLIGATION_SUBJECT
    prompt = 'Obligation Subject'
    needs_value = True
    children = [ObligationActionNode]

class NormEventNode(InputUnit):
    node_type = UnitType.NORM_EVENT
    prompt = 'Norm Event'
    needs_value = True
    children = [ObligationSubjectNode]


class ContractActionNode(InputUnit):
    node_type = UnitType.CONTRACT_ACTION
    prompt = 'Contract Action'
    needs_value = True

class ContractSubjectNode(InputUnit):
    node_type = UnitType.CONTRACT_SUBJECT
    prompt = 'Contract Subject'
    children = [ContractActionNode]

class ContractEventNode(InputUnit):
    node_type = UnitType.CONTRACT_EVENT
    prompt = 'Contract Event'
    children = [ContractSubjectNode]

class CommonEventNode(InputUnit):
    node_type = UnitType.COMMON_EVENT
    prompt = 'Common Event'
    needs_value = True
    children = [SubjectNode]

class StandardEventNode(InputUnit):
    node_type = UnitType.STANDARD_EVENT
    prompt = 'Standard Contract Event'
    children = [ContractEventNode, NormEventNode, CommonEventNode]

