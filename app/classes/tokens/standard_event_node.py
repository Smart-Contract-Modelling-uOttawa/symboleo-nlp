from app.classes.tokens.abstract_node import AbstractNode
from app.classes.tokens.node_type import NodeType
 

class ContractActionNode(AbstractNode):
    node_type = NodeType.CONTRACT_ACTION
    prompt = 'Contract Action'
    needs_value = True
    # This requires options... May be init'd...

class ContractSubjectNode(AbstractNode):
    node_type = NodeType.CONTRACT_SUBJECT
    prompt = 'Contract Subject'
    children = [ContractActionNode]

class ContractEventNode(AbstractNode):
    node_type = NodeType.CONTRACT_EVENT
    prompt = 'Contract Event'
    children = [ContractSubjectNode]

class StandardEventNode(AbstractNode):
    node_type = NodeType.STANDARD_EVENT
    prompt = 'Standard Contract Event'
    children = [ContractEventNode]

