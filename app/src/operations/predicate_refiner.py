from app.classes.symboleo_contract import SymboleoContract
from app.src.operations.configs import PredicateProcessorConfig
from app.src.operations.helpers.predicate_processor import IProcessPredicates
from app.classes.spec.predicate_function import PredicateFunction

class IRefinePredicates:
    def refine(self, config: PredicateProcessorConfig, contract: SymboleoContract, predicate: PredicateFunction) -> SymboleoContract:
        raise NotImplementedError()

class PredicateRefiner:
    def __init__(
        self,
        predicate_processor: IProcessPredicates
    ):
        self.__processor = predicate_processor
    
    def refine(self, config: PredicateProcessorConfig, contract: SymboleoContract, predicate: PredicateFunction) -> SymboleoContract:
        result = self.__processor.process(config, contract, predicate)
        return result
