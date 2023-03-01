from __future__ import annotations
from typing import List
import copy
from app.classes.grammar.node_type import NodeType
from app.src.operations.configs import OpCode

class Frame:
    pattern: List[NodeType]
    op_code: OpCode

    def to_text(self) -> str:
        raise NotImplementedError()
    
    def is_complete(self) -> bool:
        return False
    
    @staticmethod
    def copy(frame: Frame):
        return copy.deepcopy(frame)
    

    
