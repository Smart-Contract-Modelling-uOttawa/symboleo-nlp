from typing import Dict 
from enum import Enum
from app.classes.symboleo_contract import SymboleoContract
from app.src.operations.contract_updater import IUpdateContractOp
from app.src.operations.parm_operations.configs import ParameterConfig

class ParmOpCode(Enum):
    ADD_DM_PROP = 1 # TODO: May actually remove this one...
    REFINE_PREDICATE = 2
    ADD_TRIGGER = 3
    ADD_NORM = 4 

class ParameterOperation:
    def __init__(self, op_code: ParmOpCode, config: ParameterConfig, update_obj: any):
        self.op_code = op_code 
        self.config = config
        self.update_obj = update_obj

class IUpdateParameter:
    def update(self, contract: SymboleoContract, config: ParameterConfig, update_obj: any):
        raise NotImplementedError()


class ParameterUpdater(IUpdateContractOp):
    def __init__(
        self,
        predicate_refiner: IUpdateParameter,
        trigger_adder: IUpdateParameter,
        norm_adder: IUpdateParameter,
        dm_prop_adder: IUpdateParameter
    ):
        self.__op_dict: Dict[ParmOpCode, IUpdateParameter] = {
            ParmOpCode.ADD_DM_PROP: dm_prop_adder,
            ParmOpCode.ADD_NORM: norm_adder,
            ParmOpCode.ADD_TRIGGER: trigger_adder,
            ParmOpCode.REFINE_PREDICATE: predicate_refiner
        }

    def update(self, contract: SymboleoContract, operation: ParameterOperation) -> SymboleoContract:
        op = self.__op_dict[operation.op_code]
        return op.update(contract, operation.config, operation.update_obj)
    