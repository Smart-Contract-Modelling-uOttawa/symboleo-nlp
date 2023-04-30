from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode

from app.src.operations.refine_parameter.parameter_refiner import IRefineParameter, ParameterOperation
from app.src.operations.domain_updater import IUpdateDomain, DomainOperation
from app.src.operations.termination_updater import IAddPower, TerminationOperation
from app.src.grammar.input_converter import IConvertInput

class ContractUpdater:
    def __init__(
        self, 
        input_converter: IConvertInput,
        parm_refiner: IRefineParameter,
        tp_adder: IAddPower,
        domain_updater: IUpdateDomain
    ):
        self.__input_converter = input_converter
        self.__parm_refiner = parm_refiner
        self.__domain_updater = domain_updater
        self.__tp_adder = tp_adder


    def update(self, contract: SymboleoContract, op_code: OpCode, config: UpdateConfig):
        node_list = self.__input_converter.convert(config.node_list)

        if op_code == OpCode.UPDATE_PARM:
            parm_op = ParameterOperation(config.parm_key, node_list)
            self.__parm_refiner.refine(contract, parm_op)
        
        elif op_code == OpCode.ADD_DOMAIN_OBJECT:
            domain_op = DomainOperation(config.domain_object, config.declaration)
            self.__domain_updater.update(contract, domain_op)

        elif op_code == OpCode.ADD_TERMINATION_POWER:
            term_op = TerminationOperation(config.norm_id, config.debtor, config.creditor, node_list)
            self.__tp_adder.update(contract, term_op)

        else:
            raise ValueError('Invalid operation requested.')