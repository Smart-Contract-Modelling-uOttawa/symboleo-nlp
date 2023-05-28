from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

from app.classes.units.event_node import EventNode
from app.classes.units.date_node import DateNode
from app.classes.units.timepoint_node import TimepointNode

from app.classes.elements.before_node import BeforeNode as Target

class BeforeNode(InputUnit):
    node_type = UnitType.BEFORE
    sn_type = Target
    prompt = 'before'
    init_value = 'before'
    children = [EventNode, DateNode, TimepointNode]

