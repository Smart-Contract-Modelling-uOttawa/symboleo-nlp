from app.src.operations.parm_operations.parameter_updater import IUpdateParameter
from app.classes.symboleo_contract import SymboleoContract
from app.src.operations.parm_operations.configs import ParameterConfig
from app.src.operations.helpers.predicate_processor import IProcessPredicates
from app.classes.spec.predicate_function import PredicateFunction

class PredicateRefiner(IUpdateParameter):
    def __init__(
        self,
        predicate_processor: IProcessPredicates
    ):
        self.__processor = predicate_processor
    

    def update(self, contract: SymboleoContract, config: ParameterConfig, update_obj: PredicateFunction):
        result = self.__processor.process(config, contract, update_obj)
        return result
