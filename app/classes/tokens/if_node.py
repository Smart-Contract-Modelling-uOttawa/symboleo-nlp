from app.classes.tokens.abstract_node import AbstractNode
from app.classes.tokens.node_type import NodeType

from app.classes.tokens.event_node import EventNode

from app.classes.selection.if_node import IfNode as Target

class IfNode(AbstractNode):
    node_type = NodeType.IF
    sn_type = Target
    prompt = 'If'
    init_value = 'if'
    children = [EventNode]
