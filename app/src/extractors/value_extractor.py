from typing import TypeVar, Generic
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.units.node_type import *

T = TypeVar('T')

class IExtractValue(Generic[T]):
    def extract(self, str_val: str, contract: SymboleoContract = None) -> T:
        raise NotImplementedError()
    

class DefaultExtractor(IExtractValue[str]):
    def extract(self, str_val: str, contract: SymboleoContract = None) -> str:
        return str_val



