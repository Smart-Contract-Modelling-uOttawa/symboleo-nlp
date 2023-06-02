from typing import List
from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.units.root_unit import RootUnit

from app.classes.elements.element import Element
from app.classes.elements.static_elements import FinalElement, RootElement

from app.src.selection.child_node_getter import IGetNodeChildren
from app.src.selection.token_selector_set import ISelectNode
from app.src.selection.input_value_getter import IGetInputValues
from app.src.selection.element_extractor import IExtractElements

# TODO: F3? - Will need to integrate the CommonEvent handling stuff in though...
class ISelectElementList:
    def select(self, contract: ISymboleoContract) -> List[Element]:
        raise NotImplementedError()
    
class ElementListSelector(ISelectElementList):
    def __init__(
        self, 
        child_node_getter: IGetNodeChildren,
        child_selector: ISelectNode,
        input_value_getter: IGetInputValues,
        element_extractor: IExtractElements
    ):
        self.__child_node_getter = child_node_getter
        self.__child_selector = child_selector
        self.__value_getter = input_value_getter
        self.__element_extractor = element_extractor

    def select(self, contract: ISymboleoContract) -> List[Element]:
        unit = RootUnit()
        results: List[Element] = [RootElement()]
        element = None

        while (True):
            children = self.__child_node_getter.get(unit, element, contract)

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
