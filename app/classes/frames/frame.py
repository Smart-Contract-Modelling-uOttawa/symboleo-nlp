from __future__ import annotations
from typing import List
import copy
from app.classes.tokens.node_type import NodeType
from app.src.operations.refine_parameter.parm_configs import ParmOpCode

class Frame: # pragma: no cover
    pattern: List[NodeType]
    op_code: ParmOpCode

    def to_text(self) -> str:
        raise NotImplementedError()
    
    def is_complete(self) -> bool:
        return False
    
    @staticmethod
    def copy(frame: Frame):
        return copy.deepcopy(frame)
    

class DummyFrame(Frame):
    pattern = [NodeType.ROOT]
    op_code = ParmOpCode.REFINE_PREDICATE
    test_value: str = ''

    def is_complete(self):
        return self.test_value != '' 

    def to_text(self):
        return f'DUMMY: {self.test_value}'
    
    
