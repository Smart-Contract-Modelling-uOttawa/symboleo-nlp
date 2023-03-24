from enum import Enum
from typing import Dict
from app.classes.symboleo_contract import SymboleoContract

class OpCode(Enum):
    UPDATE_PARM = 1
    ADD_TERMINATION_POWER = 2
    ADD_DOMAIN_OBJECT = 3


class ContractOperation:
    def __init__(self, op_code: OpCode, update_obj: any):
        self.op_code = op_code
        self.update_obj = update_obj # May need to type this more strongly


class IUpdateContractOp:
    def update(self, contract: SymboleoContract, update_obj: any) -> SymboleoContract:
        raise NotImplementedError()


class IUpdateContracts:
    def update(self, contract: SymboleoContract, operation: ContractOperation) -> SymboleoContract:
       raise NotImplementedError()


class ContractUpdater(IUpdateContracts):
    def __init__(
        self, 
        parm_updater: IUpdateContractOp,
        tp_adder: IUpdateContractOp,
        do_adder: IUpdateContractOp
    ):
        self.__op_dict: Dict[OpCode, IUpdateContractOp] = {
            OpCode.UPDATE_PARM: parm_updater,
            OpCode.ADD_TERMINATION_POWER: tp_adder,
            OpCode.ADD_DOMAIN_OBJECT: do_adder
        }


    def update(self, contract: SymboleoContract, operation: ContractOperation):
        op = self.__op_dict[operation.op_code]
        return op.update(contract, operation.update_obj)