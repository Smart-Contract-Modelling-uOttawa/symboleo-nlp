from app.classes.tokens.abstract_node import AbstractNode
from app.classes.tokens.node_type import NodeType

from app.classes.tokens.event_node import EventNode
from app.classes.tokens.date_node import DateNode
from app.classes.tokens.timepoint_node import TimepointNode

from app.classes.selection.before_node import BeforeNode as Target

class BeforeNode(AbstractNode):
    node_type = NodeType.BEFORE
    sn_type = Target
    prompt = 'before'
    init_value = 'before'
    children = [EventNode, DateNode, TimepointNode]

