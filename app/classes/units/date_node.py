from app.classes.units.input_unit import InputUnit
from app.classes.units.node_type import NodeType

from app.classes.selection.date_node import DateNode as Target

class DateNode(InputUnit):
    node_type = NodeType.DATE
    sn_type = Target
    prompt = 'Enter a date'
    needs_value = True
