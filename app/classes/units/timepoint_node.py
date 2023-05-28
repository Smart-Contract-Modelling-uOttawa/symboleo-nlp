
from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

from app.classes.elements.timepoint_node import TimepointNode as Target

class TimepointNode(InputUnit):
    node_type = UnitType.TIMEPOINT
    sn_type = Target
    prompt = 'Specify a timepoint'
    needs_value = True
