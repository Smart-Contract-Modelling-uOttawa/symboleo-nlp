from __future__ import annotations
from typing import List, Type
from app.classes.selection.selected_node import SelectedNode
from app.classes.units.node_type import NodeType

class InputUnit: # pragma: no cover
    id: str = None
    sn_type: Type[SelectedNode] = SelectedNode # Might be able to remove this
    node_type: NodeType = None
    prompt: str = None
    children: List[Type[SelectedNode]] = []
    needs_value = False
    init_value = ''
    options: List[str] = None
    # TODO: options...
    
    def __init__(self, options: List[str] = None):
        self.options = options 
    
    def __eq__(self, other: InputUnit) -> bool:
        return self.node_type == other.node_type # more here?

    def get_value(self):
        raise NotImplementedError()
    

class DummyNode(InputUnit):
    prompt = 'dummy'
    node_type = NodeType.DUMMY
