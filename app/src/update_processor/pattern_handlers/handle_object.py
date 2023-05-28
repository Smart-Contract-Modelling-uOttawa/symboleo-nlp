from typing import List
from app.classes.spec.norm import Norm
from app.classes.elements.element import Element

# TODO: Move to clsases

class HandleObject:
    def __init__(
        self,
        norm: Norm
    ):
        self.norm = norm
        