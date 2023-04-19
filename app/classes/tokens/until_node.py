from typing import List
from app.classes.tokens.abstract_node import AbstractNode
from app.classes.tokens.node_type import NodeType

from app.classes.tokens.event_node import EventNode

from app.classes.selection.until_node import UntilNode as Target

class UntilNode(AbstractNode):
    sn_type = Target
    prompt = 'Until'
    init_value = 'until'
    children = [EventNode]