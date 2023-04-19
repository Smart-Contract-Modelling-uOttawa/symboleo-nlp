from app.classes.tokens.abstract_node import AbstractNode
from app.classes.tokens.node_type import NodeType

from app.classes.tokens.standard_event_node import StandardEventNode
from app.classes.tokens.new_event_node import NewEventNode

from app.classes.selection.event_node import EventNode as Target

class EventNode(AbstractNode):
    node_type = NodeType.EVENT
    sn_type = Target
    prompt = 'Describe an event'
    children = [StandardEventNode, NewEventNode]