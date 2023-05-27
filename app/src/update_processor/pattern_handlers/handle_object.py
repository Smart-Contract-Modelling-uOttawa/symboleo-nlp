from typing import List
from app.classes.spec.norm import Norm
from app.classes.selection.selected_node import SelectedNode

# TODO: Move to clsases

class HandleObject:
    def __init__(
        self,
        norm: Norm
    ):
        self.norm = norm
        