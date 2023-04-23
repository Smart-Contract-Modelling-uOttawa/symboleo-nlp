from typing import TypeVar, Generic
from app.classes.tokens.node_type import *

T = TypeVar('T')

class IExtractValue(Generic[T]):
    def extract(self, str_val: T):
        raise NotImplementedError()
    

class DefaultExtractor(IExtractValue[str]):
    def extract(self, str_val: str):
        return str_val



