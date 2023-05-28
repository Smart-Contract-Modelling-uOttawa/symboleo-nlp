from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

from app.classes.units.event_node import EventNode

from app.classes.elements.if_node import IfNode as Target

class IfNode(InputUnit):
    node_type = UnitType.IF
    sn_type = Target
    prompt = 'If'
    init_value = 'if'
    children = [EventNode]
