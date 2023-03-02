from typing import List
from app.src.operations.configs import OpCode

class GrammarGeneratorConfig:
    def __init__(self, op_codes: List[OpCode] = None):
        if not op_codes:
            self.op_codes = [OpCode.ADD_TRIGGER, OpCode.REFINE_PREDICATE, OpCode.ADD_NORM, OpCode.ADD_DM_PROP] 
        else:
            self.op_codes = op_codes
