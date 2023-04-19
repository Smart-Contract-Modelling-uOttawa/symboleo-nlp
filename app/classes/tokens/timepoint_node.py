from app.classes.tokens.abstract_node import AbstractNode
from app.classes.tokens.node_type import NodeType

from app.classes.selection.timepoint_node import TimepointNode as Target

class TimepointNode(AbstractNode):
    sn_type = Target
    prompt = 'Specify a timepoint'
    needs_value = True
