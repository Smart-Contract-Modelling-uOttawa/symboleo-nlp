from typing import List
from app.classes.tokens.abstract_node import AbstractNode
from app.classes.tokens.node_type import NodeType
 
from app.classes.tokens.contract_subject_node import ContractSubjectNode

from app.classes.selection.standard_event_node import StandardEventNode as Target
 
# TODO: Lots of work todo on here
 # I want this one to refer to ALL contract events - contract/obligation/power...
 # potentially also the common contract events as well...
 ## The point is that they have predictable/pre-determined NL structures

class StandardEventNode(AbstractNode):
    node_type = NodeType.STANDARD_EVENT
    sn_type = Target
    prompt = 'Standard Contract Event'
    children = [ContractSubjectNode]

