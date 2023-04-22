from __future__ import annotations
from typing import List, Type
from app.classes.selection.selected_node import SelectedNode
from app.classes.tokens.node_type import NodeType

class AbstractNode: # pragma: no cover
    id: str = None
    sn_type: Type[SelectedNode] = SelectedNode # Might be able to remove this
    node_type: NodeType = None
    prompt: str = None
    children: List[Type[SelectedNode]] = []
    needs_value = False
    init_value = ''
    # TODO: options...
    
    # def __init__(self, id: str = '', children: List[AbstractNode] = []):
    #     self.id = id
    #     self.children = children
    
    def get_value(self):
        raise NotImplementedError()
    

class DummyNode(AbstractNode):
    def __init__(self, id: str, children: List[AbstractNode] = []):
        super().__init__(id, children)
        self.prompt = 'dummy'
        self.node_type = NodeType.DUMMY

    def get_value(self):
        result = 'dummy'   
        return result