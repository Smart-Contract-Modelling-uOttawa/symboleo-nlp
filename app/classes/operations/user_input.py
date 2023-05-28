from app.classes.units.unit_type import *

class UserInput:
    def __init__(self, unit_type:UnitType, value: str = None):
        self.unit_type = unit_type
        self.value = value
        