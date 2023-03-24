from typing import List
from app.src.operations.parm_operations.configs import ParmOpCode

class GrammarGeneratorConfig:
    def __init__(self, op_codes: List[ParmOpCode] = None):
        if not op_codes:
            self.op_codes = [ParmOpCode.ADD_TRIGGER, ParmOpCode.REFINE_PREDICATE, ParmOpCode.ADD_NORM, ParmOpCode.ADD_DM_PROP] 
        else:
            self.op_codes = op_codes
