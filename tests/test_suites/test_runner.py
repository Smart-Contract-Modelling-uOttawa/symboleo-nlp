from app.classes.symboleo_contract import SymboleoContract
from app.src.operations.contract_updater_builder import ContractUpdaterBuilder
from app.src.operations.contract_updater import OpCode, ContractOperation

from app.src.operations.parm_operations.configs import ParameterConfig
from app.src.grammar.selection import Selection
from app.src.operations.helpers.default_event_getter import DefaultEventGetter
from app.src.frames.frame_checker_constuctor import FrameCheckerConstructor
from app.src.operations.parm_operations.parameter_operation_extractor import ParameterOperationExtractor

class TestConfig:
    def __init__(
            self, 
            op_code: OpCode, 
            selection: Selection = None, 
            parm_config: ParameterConfig = None,
        ):
        self.op_code = op_code
        self.selection: Selection = selection
        self.parm_config: ParameterConfig = parm_config


class TestRunner:
    def __init__(self):
        frame_checker = FrameCheckerConstructor.construct()
        default_event_getter = DefaultEventGetter()

        self.__parameter_operation_extractor = ParameterOperationExtractor(
            frame_checker,
            default_event_getter
        )

        # Others...

        self.__contract_updater = ContractUpdaterBuilder.build()
    
    def update_contract(self, contract: SymboleoContract, config: TestConfig) -> SymboleoContract:
        update_obj = self._create_update_obj(contract, config)
        contract_operation = ContractOperation(config.op_code, update_obj)
        contract = self.__contract_updater.update(contract, contract_operation)
        return contract


    def _create_update_obj(self, contract: SymboleoContract, config: TestConfig):
        # Each of these will likely be pulled out on its own
        if config.op_code == OpCode.UPDATE_PARM:
            update_obj = self.__parameter_operation_extractor.extract(contract, config.parm_config, config.selection)

        elif config.op_code == OpCode.ADD_DOMAIN_OBJECT:
            update_obj = None
        
        elif config.op_code == OpCode.ADD_TERMINATION_POWER:
            update_obj = None

        else:
            raise ValueError('Invalid op code')

        return update_obj
    
