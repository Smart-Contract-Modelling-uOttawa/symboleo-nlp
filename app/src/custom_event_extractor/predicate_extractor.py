from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.events.custom_event.predicate import Predicate
from app.src.custom_event_extractor.element_extractor import IExtractElement

class PredicateExtractor(IExtractElement[Predicate]):    
    def __init__(self):
        self.__nlp = None

    def extract(self, str_val: str, contract: SymboleoContract = None) -> Predicate:
        return Predicate(str_val)
