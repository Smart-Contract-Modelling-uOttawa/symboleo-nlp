from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

from app.classes.units.standard_event_node import StandardEventNode
from app.classes.units.custom_event_node import CustomEventNode

from app.classes.elements.event_node import EventNode as Target

class EventNode(InputUnit):
    node_type = UnitType.EVENT
    sn_type = Target
    prompt = 'Describe an event'
    children = [StandardEventNode, CustomEventNode]