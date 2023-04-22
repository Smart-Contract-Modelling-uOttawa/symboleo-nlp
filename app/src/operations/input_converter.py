from typing import List
from app.classes.operations.user_input import UserInput, NodeType
from app.classes.selection.all_nodes import *

from app.src.extractors.value_extractor import IExtractValue

class IConvertInput:
    def convert(self, input: List[UserInput]) -> List[SelectedNode]:
        raise NotImplementedError()

class InputConverter(IConvertInput):
    def __init__(self, extractor_dict: Dict[NodeType, IExtractValue]):
        self.__dict = extractor_dict

    def convert(self, input: List[UserInput]) -> List[SelectedNode]:
        results = []

        for x in input:
            op = self.__dict[x.node_type]
            val = op.extract(x.value)
            next_type = node_type_to_class[x.node_type]
            next_result = next_type(val)
            results.append(next_result)
        
        return results
