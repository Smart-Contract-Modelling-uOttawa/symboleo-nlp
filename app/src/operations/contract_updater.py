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
        norms = contract.get_norms_by_key(config.nl_key, config.parm_key)
        norm = norms[0]

        if op_code == OpCode.UPDATE_PARM:
            update_obj = self.__operation_mapper.map(config.user_inputs, contract, norm)
            contract.run_updates(update_obj)
            contract.update_nl(config.nl_key, config.parm_key, update_obj.nl_update)
        
        # elif op_code == OpCode.ADD_TERMINATION_POWER:
        #     term_op = TerminationOperation(config.norm_id, config.debtor, config.creditor, elements)
        #     self.__tp_adder.update(contract, term_op)

        else:
            raise ValueError('Invalid operation requested.')
    