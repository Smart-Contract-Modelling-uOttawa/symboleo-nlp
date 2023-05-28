from app.classes.spec.symboleo_contract import ISymboleoContract

from app.src.grammar.element_list_selector import ISelectElementList
from app.src.operations.refine_parameter.parameter_refiner_new import IRefineParameter, ParameterOperation

class ParameterRefiner:
    def __init__(
        self,
        elements_selector: ISelectElementList,
        parm_refiner: IRefineParameter,
        
    ):
        self.__elements_selector = elements_selector
        self.__parm_refiner = parm_refiner

    def refine(self, contract: ISymboleoContract, nl_key: str, parm_key: str):
        # Gather input: List of values
        elements = self.__elements_selector.select(contract)

        self.__parm_refiner.refine(
            contract, 
            ParameterOperation(nl_key, parm_key, elements)
        )
