from app.classes.tokens.abstract_node import AbstractNode
from app.classes.tokens.node_type import NodeType

from app.classes.selection.contract_action_node import ContractActionNode as Target

class ContractActionNode(AbstractNode):
    node_type = NodeType.CONTRACT_ACTION
    sn_type = Target
    prompt = 'Contract Action'
    needs_value = True
