from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

from app.classes.units.custom_event_node import VerbNode

from app.classes.elements.custom_event_node import FailsToNode as Target

class FailsToNode(InputUnit):
    node_type = UnitType.FAILS_TO
    sn_type = Target
    prompt = 'fails to'
    init_value = 'fails to'
    children = [VerbNode]