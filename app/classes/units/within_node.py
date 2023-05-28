from app.classes.units.input_unit import InputUnit
from app.classes.units.node_type import NodeType

from app.classes.units.timespan_node import TimespanNode

from app.classes.elements.within_node import WithinNode as Target

class WithinNode(InputUnit):
    node_type = NodeType.WITHIN
    sn_type = Target
    prompt = 'Within'
    init_value = 'within'
    children = [TimespanNode]