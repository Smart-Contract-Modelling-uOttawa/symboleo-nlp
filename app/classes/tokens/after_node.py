from app.classes.tokens.abstract_node import AbstractNode
from app.classes.tokens.node_type import NodeType

from app.classes.tokens.event_node import EventNode
from app.classes.tokens.date_node import DateNode
from app.classes.tokens.timepoint_node import TimepointNode

from app.classes.selection.after_node import AfterNode as Target

class AfterNode(AbstractNode):
    node_type = NodeType.AFTER
    sn_type = Target
    prompt = 'after'
    init_value = 'after'
    children = [EventNode, DateNode, TimepointNode]