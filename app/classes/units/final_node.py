from typing import List
from app.classes.units.input_unit import InputUnit
from app.classes.units.node_type import NodeType

class FinalNode(InputUnit):
    node_type = NodeType.FINAL_NODE
    prompt = 'FINISH'
    needs_value = False
    init_value = 'X'
