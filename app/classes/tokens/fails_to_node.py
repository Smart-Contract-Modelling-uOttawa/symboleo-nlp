from app.classes.tokens.abstract_node import AbstractNode
from app.classes.tokens.node_type import NodeType

from app.classes.tokens.custom_event_node import VerbNode

from app.classes.selection.custom_event_node import FailsToNode as Target

class FailsToNode(AbstractNode):
    node_type = NodeType.FAILS_TO
    sn_type = Target
    prompt = 'fails to'
    init_value = 'fails to'
    children = [VerbNode]