from typing import List
from app.classes.operations.op_code import OpCode
from app.classes.operations.user_input import UserInput

class UpdateConfig:
    def __init__(
            self, 
            op_code: OpCode = None, 
            user_inputs: List[UserInput] = None,
            nl_key: str = None,
            parm_key: str = None,
        ):
        self.op_code = op_code
        self.user_inputs = user_inputs
        self.nl_key = nl_key
        self.parm_key = parm_key
