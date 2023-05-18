from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.custom_event.predicate import Predicate
from app.src.extractors.value_extractor import IExtractValue

class PredicateExtractor(IExtractValue[Predicate]):    
    def __init__(self):
        self.__nlp = None

    def extract(self, str_val: str, contract: SymboleoContract = None) -> Predicate:
        return Predicate(str_val)
