from typing import List
from app.classes.units.input_unit import InputUnit
from app.classes.units.node_type import NodeType

from app.classes.units.event_node import EventNode

from app.classes.selection.until_node import UntilNode as Target

class UntilNode(InputUnit):
    node_type = NodeType.UNTIL
    sn_type = Target
    prompt = 'Until'
    init_value = 'until'
    children = [EventNode]