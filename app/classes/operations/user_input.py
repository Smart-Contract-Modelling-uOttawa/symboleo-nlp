from app.classes.units.unit_type import *

class UserInput:
    def __init__(self, node_type:UnitType, value: str = None):
        self.node_type = node_type
        self.value = value
        