from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode

from app.src.operations.operation_mapper import IMapCnlToOperations

class IUpdateContract:
    def update(self, contract: SymboleoContract, op_code: OpCode, config: UpdateConfig):
        raise NotImplementedError()


class ContractUpdater(IUpdateContract):
    def __init__(
        self, 
        operation_mapper: IMapCnlToOperations
    ):
        self.__operation_mapper = operation_mapper


    def update(self, contract: SymboleoContract, op_code: OpCode, config: UpdateConfig):
        # Need to get the norm
        norm_configs = contract.get_norm_configs_by_key(config.nl_key, config.parm_key)
        
        for norm_config in norm_configs:

            if op_code == OpCode.UPDATE_PARM:
                update_obj = self.__operation_mapper.map(config.user_inputs, contract, norm_config)
                contract.run_updates(update_obj)
                contract.update_nl(config.nl_key, config.parm_key, update_obj.nl_update)

            else:
                raise ValueError('Invalid operation requested.')
    