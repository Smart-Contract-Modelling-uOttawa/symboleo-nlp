from app.classes.units.input_unit import InputUnit
from app.classes.units.node_type import NodeType

from app.classes.units.event_node import EventNode
from app.classes.units.date_node import DateNode
from app.classes.units.timepoint_node import TimepointNode

from app.classes.selection.before_node import BeforeNode as Target

class BeforeNode(InputUnit):
    node_type = NodeType.BEFORE
    sn_type = Target
    prompt = 'before'
    init_value = 'before'
    children = [EventNode, DateNode, TimepointNode]

