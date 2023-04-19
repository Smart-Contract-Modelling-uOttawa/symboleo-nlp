from app.classes.tokens.abstract_node import AbstractNode
from app.classes.tokens.node_type import NodeType

from app.classes.tokens.contract_action_node import ContractActionNode

from app.classes.selection.contract_subject_node import ContractSubjectNode as Target

class ContractSubjectNode(AbstractNode):
    node_type = NodeType.CONTRACT_SUBJECT
    sn_type = Target
    prompt = 'Contract Subject'
    needs_value = True
    children = [ContractActionNode]
