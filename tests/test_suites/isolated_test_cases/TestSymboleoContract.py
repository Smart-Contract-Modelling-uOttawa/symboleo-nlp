from typing import List
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.declaration import Declaration
from app.classes.spec.norm import Obligation
from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode


class TestCase:
    def __init__(
        self,
        case_id: str,
        init_sym: SymboleoContract,
        op_code: OpCode,
        update_config: UpdateConfig,
        exp_sym: SymboleoContract = None
    ):
        self.case_id = case_id
        self.init_sym = init_sym
        self.op_code = op_code
        self.update_config = update_config
        self.exp_sym = exp_sym

class TestInfo:
    def __init__(
        self,
        full_nl: str,
        refinement: str, 
        declarations: List[Declaration],
        obligation: Obligation
    ):
        self.full_nl = full_nl
        self.declarations = declarations
        self.obligation = obligation

