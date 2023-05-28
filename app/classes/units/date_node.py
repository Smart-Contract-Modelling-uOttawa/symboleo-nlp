from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

from app.classes.elements.date_node import DateNode as Target

class DateNode(InputUnit):
    node_type = UnitType.DATE
    sn_type = Target
    prompt = 'Enter a date'
    needs_value = True
