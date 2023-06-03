from typing import List
from app.classes.operations.user_input import UserInput, UnitType
from app.classes.elements.all_elements import *

from app.src.selection.element_extractors.element_extractor import IExtractElement

class IExtractElements:
    def extract(self, input: List[UserInput]) -> List[Element]:
        raise NotImplementedError()

    def extract_single(self, input: UserInput) -> Element:
        raise NotImplementedError

class ElementExtractor(IExtractElements):
    def __init__(self, extractor_dict: Dict[UnitType, IExtractElement]):
        self.__dict = extractor_dict

    def extract(self, input: List[UserInput]) -> List[Element]:
        return [self.extract_single(x) for x in input] 

    def extract_single(self, input: UserInput) -> Element:
        op = self.__dict[input.unit_type]
        val = op.extract(input.value)

        next_type = unit_type_to_class[input.unit_type]
        return next_type(val, input.value)

