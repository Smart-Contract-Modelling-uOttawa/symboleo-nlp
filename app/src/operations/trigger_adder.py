from app.classes.symboleo_contract import SymboleoContract
from app.src.operations.configs import ParameterConfig
from app.src.operations.helpers.predicate_processor import IProcessPredicates
from app.classes.spec.predicate_function import PredicateFunction

class IAddTriggers:
    def add(self, config: ParameterConfig, contract: SymboleoContract, predicate: PredicateFunction) -> SymboleoContract:
        raise NotImplementedError()


class TriggerAdder:
    def __init__(
        self,
        predicate_processor: IProcessPredicates
    ):
        self.__processor = predicate_processor
    
    def add(self, config: ParameterConfig, contract: SymboleoContract, predicate: PredicateFunction) -> SymboleoContract:
        config.norm_component = 'trigger'
        result = self.__processor.process(config, contract, predicate)
        return result
