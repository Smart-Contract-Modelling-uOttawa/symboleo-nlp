from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

from app.classes.units.event_node import EventNode
from app.classes.units.date_node import DateNode
from app.classes.units.timepoint_node import TimepointNode

from app.classes.elements.after_node import AfterNode as Target

class AfterNode(InputUnit):
    node_type = UnitType.AFTER
    sn_type = Target
    prompt = 'after'
    init_value = 'after'
    children = [EventNode, DateNode, TimepointNode]