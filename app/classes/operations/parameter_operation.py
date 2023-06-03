# TODO: E3? - Will likely need to specify the norm_component...
# Instead of key, can I use the ParmConfig...?
from app.classes.elements.element import Element


from typing import List


class ParameterOperation:
    def __init__(self, nl_key:str, parm_key:str, elements: List[Element]):
        self.nl_key = nl_key
        self.parm_key = parm_key
        self.elements = elements