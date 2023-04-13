from app.classes.spec.symboleo_contract import SymboleoContract
from app.src.operations.op_code import OpCode

from app.src.operations.refine_parameter.parameter_refiner import IRefineParameter, ParameterOperation
from app.src.operations.domain_updater import IUpdateDomain, DomainOperation
from app.src.operations.add_power.termination_updater import IAddPower, TerminationOperation
from app.src.operations.contract_updater_config import UpdateConfig


# Could potentially move to be a method on the SymboleoContract...
# contract.update(...)... then handle the parsing
class ContractUpdater:
    def __init__(
        self, 
        parm_refiner: IRefineParameter,
        tp_adder: IAddPower,
        domain_updater: IUpdateDomain
    ):
        self.__parm_refiner = parm_refiner
        self.__domain_updater = domain_updater
        self.__tp_adder = tp_adder


    def update(self, contract: SymboleoContract, op_code: OpCode, config: UpdateConfig):
        if op_code == OpCode.UPDATE_PARM:
            parm_op = ParameterOperation(config.parm_config, config.selection, config.parm_key)
            self.__parm_refiner.refine(contract, parm_op)
        
        elif op_code == OpCode.ADD_DOMAIN_OBJECT:
            domain_op = DomainOperation(config.domain_object, config.declaration)
            self.__domain_updater.update(contract, domain_op)

        elif op_code == OpCode.ADD_TERMINATION_POWER:
            term_op = TerminationOperation(config.norm_id, config.debtor, config.creditor, config.selection)
            self.__tp_adder.update(contract, term_op)

        else:
            raise ValueError('Invalid operation requested.')