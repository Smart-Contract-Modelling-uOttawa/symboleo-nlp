from typing import List
from app.classes.units.input_unit import InputUnit
from app.classes.units.unit_type import UnitType

class FinalNode(InputUnit):
    node_type = UnitType.FINAL_NODE
    prompt = 'FINISH'
    needs_value = False
    init_value = 'X'
