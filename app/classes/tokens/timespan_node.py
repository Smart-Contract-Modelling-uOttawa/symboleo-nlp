from typing import List
from app.classes.tokens.abstract_node import AbstractNode
from app.classes.tokens.node_type import NodeType

from app.classes.tokens.event_node import EventNode

from app.classes.selection.timespan_node import TimespanNode as Target

class TimespanNode(AbstractNode):
    sn_type = Target
    prompt = 'Enter a timespan'
    needs_value = True
    children = [EventNode]
