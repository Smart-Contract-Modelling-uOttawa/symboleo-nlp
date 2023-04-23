from typing import TypeVar, Generic
from app.classes.tokens.node_type import *

T = TypeVar('T')

# TODO: Need to strongly type the extractors - may use a generic [T]
## May also need to bring in the contract as input
class IExtractValue(Generic[T]):
    def extract(self, str_val: T):
        raise NotImplementedError()
    

class DefaultExtractor(IExtractValue[str]):
    def extract(self, str_val: str):
        return str_val



