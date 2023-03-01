from typing import List
from app.src.operations.configs import OpCode

class GrammarConfig:
    def __init__(self, op_codes: List[OpCode]):
        self.op_codes = op_codes
