from typing import List
from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.units.root_node import RootNode as RootToken

from app.classes.elements.element import Element
from app.classes.elements.final_node import FinalNode
from app.classes.elements.root_node import RootNode

from app.src.grammar.child_getter import IGetChildren
from app.src.grammar.token_selector_set import ISelectTokenFromSet
from app.src.grammar.value_getter import IGetValues # Change to IGetInputValue
from app.src.grammar.input_converter import IConvertInput # Change to IExtractElements

# This should replace the grammar_selectors and all that...
# Will need to integrate the CommonEvent handling stuff in though...
class ISelectElementList:
    def select(self, contract: ISymboleoContract) -> List[Element]:
        raise NotImplementedError()
    
class ElementListSelector(ISelectElementList):
    def __init__(
        self, 
        child_getter: IGetChildren,
        child_selector: ISelectTokenFromSet,
        input_value_getter: IGetValues,
        element_extractor: IConvertInput
    ):
        self.__child_getter = child_getter
        self.__child_selector = child_selector
        self.__value_getter = input_value_getter
        self.__element_extractor = element_extractor

    def select(self, contract: ISymboleoContract) -> List[Element]:
        node = RootToken()
        results: List[Element] = [RootNode()]
        element = None

        while (True):
            children = self.__child_getter.get(node, element, contract)

            if len(children) == 0:
                break
            elif len(children) == 1:
                node = children[0]
            else:
                node = self.__child_selector.select(children) # Involves user input
            
            input_value = self.__value_getter.get(node) # Involves user input

            # # Make a convert_single and convert_batch...
            element = self.__element_extractor.convert([input_value])[0] 

            results.append(element)
        
        results.append(FinalNode())

        return results
