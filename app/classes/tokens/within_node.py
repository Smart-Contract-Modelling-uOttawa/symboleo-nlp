from app.classes.tokens.abstract_node import AbstractNode
from app.classes.tokens.node_type import NodeType

from app.classes.tokens.timespan_node import TimespanNode

from app.classes.selection.within_node import WithinNode as Target

class WithinNode(AbstractNode):
    node_type = NodeType.WITHIN
    sn_type = Target
    prompt = 'Within'
    init_value = 'within'
    children = [TimespanNode]