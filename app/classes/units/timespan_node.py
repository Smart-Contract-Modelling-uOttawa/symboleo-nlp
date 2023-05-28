
from typing import List
from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

from app.classes.units.event_node import EventNode

from app.classes.elements.timespan_node import TimespanNode as Target

class TimespanNode(InputUnit):
    node_type = UnitType.TIMESPAN
    sn_type = Target
    prompt = 'Enter a timespan'
    needs_value = True
    children = [EventNode]
