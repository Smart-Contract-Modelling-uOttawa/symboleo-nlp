from app.classes.units.input_unit import InputUnit
from app.classes.units.node_type import NodeType

from app.classes.units.event_node import EventNode
from app.classes.units.date_node import DateNode
from app.classes.units.timepoint_node import TimepointNode

from app.classes.selection.after_node import AfterNode as Target

class AfterNode(InputUnit):
    node_type = NodeType.AFTER
    sn_type = Target
    prompt = 'after'
    init_value = 'after'
    children = [EventNode, DateNode, TimepointNode]