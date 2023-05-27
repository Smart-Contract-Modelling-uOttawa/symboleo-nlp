from app.classes.spec.symboleo_contract import ISymboleoContract

from app.src.grammar.grammar_selector2 import ISelectGrammar
from app.src.operations.refine_parameter.parameter_refiner_new import IRefineParameter, ParameterOperation

class ParameterRefiner:
    def __init__(
        self,
        node_selector: ISelectGrammar,
        parm_refiner: IRefineParameter,
        
    ):
        self.__node_selector = node_selector
        self.__parm_refiner = parm_refiner

    def refine(self, contract: ISymboleoContract, nl_key: str, parm_key: str):
        # Gather input: List of values
        node_list = self.__node_selector.select(contract)

        self.__parm_refiner.refine(
            contract, 
            ParameterOperation(nl_key, parm_key, node_list)
        )
