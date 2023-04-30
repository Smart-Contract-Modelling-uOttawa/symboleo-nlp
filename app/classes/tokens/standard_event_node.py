from app.classes.tokens.abstract_node import AbstractNode
from app.classes.tokens.node_type import NodeType
from app.classes.tokens.custom_event_node import SubjectNode

class ObligationActionNode(AbstractNode):
    node_type = NodeType.OBLIGATION_ACTION
    prompt = 'Obligation Action'
    needs_value = True

class ObligationSubjectNode(AbstractNode):
    node_type = NodeType.OBLIGATION_SUBJECT
    prompt = 'Obligation Subject'
    needs_value = True
    children = [ObligationActionNode]

class NormEventNode(AbstractNode):
    node_type = NodeType.NORM_EVENT
    prompt = 'Norm Event'
    needs_value = True
    children = [ObligationSubjectNode]


class ContractActionNode(AbstractNode):
    node_type = NodeType.CONTRACT_ACTION
    prompt = 'Contract Action'
    needs_value = True

class ContractSubjectNode(AbstractNode):
    node_type = NodeType.CONTRACT_SUBJECT
    prompt = 'Contract Subject'
    children = [ContractActionNode]

class ContractEventNode(AbstractNode):
    node_type = NodeType.CONTRACT_EVENT
    prompt = 'Contract Event'
    children = [ContractSubjectNode]

class CommonEventNode(AbstractNode):
    node_type = NodeType.COMMON_EVENT
    prompt = 'Common Event'
    needs_value = True
    children = [SubjectNode]

class StandardEventNode(AbstractNode):
    node_type = NodeType.STANDARD_EVENT
    prompt = 'Standard Contract Event'
    children = [ContractEventNode, NormEventNode, CommonEventNode]

