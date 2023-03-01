
# Will likely scrap this entire file
from enum import Enum
from app.src.operations.configs import PredicateProcessorConfig, DomainPropProcessorConfig

# class syntax
class ContractParamType(Enum):
    TIMEFRAME = 1
    CONDITION = 2

class DomainParamType(Enum):
    LOCATION = 1
    AMOUNT = 2
    CURRENCY = 3

class Parameter:
    def __init__(self):
        param_type: any = None
        config: any = None

class ContractSpecParameter(Parameter):
    def __init__(
        self,
        param_type: ContractParamType,
        config: PredicateProcessorConfig
    ):
        self.param_type = param_type
        self.config = config
    
    
class DomainParameter(Parameter):
    def __init__(
        self,
        param_type: DomainParamType,
        config: DomainPropProcessorConfig
    ):
        self.param_type = param_type
        self.config = config