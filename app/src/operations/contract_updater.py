import copy
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.operations.contract_updater_config import UpdateConfig
from app.classes.operations.op_code import OpCode
from app.classes.operations.parameter_operation import ParameterOperation

from app.src.operations.parameter_refiner import IRefineParameter
from app.src.operations.domain_updater import IUpdateDomain, DomainOperation
from app.src.operations.termination_updater import IAddPower, TerminationOperation
from app.src.selection.element_extractor import IExtractElements
from app.src.operations.user_input_cleaner import ICleanUserInput

class ContractUpdater:
    def __init__(
        self, 
        input_cleaner: ICleanUserInput,
        element_extractor: IExtractElements,
        parm_refiner: IRefineParameter,
        tp_adder: IAddPower,
        domain_updater: IUpdateDomain
    ):
        self.__input_cleaner = input_cleaner
        self.__element_extractor = element_extractor
        self.__parm_refiner = parm_refiner
        self.__domain_updater = domain_updater
        self.__tp_adder = tp_adder


    def update(self, contract: SymboleoContract, op_code: OpCode, config: UpdateConfig):
        user_inputs = self.__input_cleaner.clean(config.user_inputs)
        elements = self.__element_extractor.extract(user_inputs)
        if op_code == OpCode.UPDATE_PARM:
            parm_op = ParameterOperation(config.nl_key, config.parm_key, elements)
            self.__parm_refiner.refine(contract, parm_op)
        
        elif op_code == OpCode.ADD_DOMAIN_OBJECT:
            domain_op = DomainOperation(config.domain_object, config.declaration)
            self.__domain_updater.update(contract, domain_op)

        elif op_code == OpCode.ADD_TERMINATION_POWER:
            term_op = TerminationOperation(config.norm_id, config.debtor, config.creditor, elements)
            self.__tp_adder.update(contract, term_op)

        else:
            raise ValueError('Invalid operation requested.')