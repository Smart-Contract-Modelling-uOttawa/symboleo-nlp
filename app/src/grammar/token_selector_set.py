from typing import List
from app.classes.units.input_unit import InputUnit

class ISelectTokenFromSet:
    def select(self, node_set: List[InputUnit]) -> InputUnit:
        raise NotImplementedError()
