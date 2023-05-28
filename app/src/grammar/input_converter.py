from typing import List
from app.classes.operations.user_input import UserInput, UnitType
from app.classes.elements.all_elements import *

from app.src.extractors.value_extractor import IExtractValue

class IConvertInput:
    def convert(self, input: List[UserInput]) -> List[Element]:
        raise NotImplementedError()

# TODO: Rename to ElementExtractor
class InputConverter(IConvertInput):
    def __init__(self, extractor_dict: Dict[UnitType, IExtractValue]):
        self.__dict = extractor_dict

    def convert(self, input: List[UserInput]) -> List[Element]:
        results = []

        for x in input:
            op = self.__dict[x.unit_type]
            val = op.extract(x.value)
            next_type = unit_type_to_class[x.unit_type]
            next_result = next_type(val)
            results.append(next_result)
        
        return results
