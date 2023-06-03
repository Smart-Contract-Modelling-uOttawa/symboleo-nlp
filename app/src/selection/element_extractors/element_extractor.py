from typing import TypeVar, Generic
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.units.unit_type import *

T = TypeVar('T')

class IExtractElement(Generic[T]):
    def extract(self, str_val: str, contract: SymboleoContract = None) -> T:
        raise NotImplementedError()
    

class DefaultExtractor(IExtractElement[str]):
    def extract(self, str_val: str, contract: SymboleoContract = None) -> str:
        return str_val



