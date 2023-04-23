from typing import List
from app.classes.operations.contract_update_obj import ContractUpdateObj
from app.classes.operations.user_input import UserInput

class NodeTestSpec:
    def __init__(
        self,
        user_input: List[UserInput],
        expected_nl: str,
        update_obj: ContractUpdateObj    
    ):
        self.user_input = user_input
        self.expected_nl = expected_nl
        self.update_obj = update_obj