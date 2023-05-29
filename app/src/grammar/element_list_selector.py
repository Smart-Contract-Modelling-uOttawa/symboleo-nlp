from typing import List
from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.units.root_unit import RootUnit

from app.classes.elements.element import Element
from app.classes.elements.static_elements import FinalElement, RootElement

from app.src.grammar.child_getter import IGetChildren
from app.src.grammar.token_selector_set import ISelectTokenFromSet
from app.src.grammar.input_value_getter import IGetInputValues
from app.src.grammar.element_extractor import IExtractElements

# Will need to integrate the CommonEvent handling stuff in though...
class ISelectElementList:
    def select(self, contract: ISymboleoContract) -> List[Element]:
        raise NotImplementedError()
    
class ElementListSelector(ISelectElementList):
    def __init__(
        self, 
        child_getter: IGetChildren,
        child_selector: ISelectTokenFromSet,
        input_value_getter: IGetInputValues,
        element_extractor: IExtractElements
    ):
        self.__child_getter = child_getter
        self.__child_selector = child_selector
        self.__value_getter = input_value_getter
        self.__element_extractor = element_extractor

    def select(self, contract: ISymboleoContract) -> List[Element]:
        unit = RootUnit()
        results: List[Element] = [RootElement()]
        element = None

        while (True):
            children = self.__child_getter.get(unit, element, contract)

            if len(children) == 0:
                break
            elif len(children) == 1:
                unit = children[0]
            else:
                unit = self.__child_selector.select(children) # Involves user input
            
            input_value = self.__value_getter.get(unit) # Involves user input

            element = self.__element_extractor.extract_single(input_value) 

            results.append(element)
        
        results.append(FinalElement())

        return results
