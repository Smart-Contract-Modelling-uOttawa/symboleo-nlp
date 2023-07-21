from app.classes.spec.symboleo_contract import SymboleoContract
from app.src.element_extractors.element_extractor import IExtractElement
from app.classes.events.custom_event.custom_event import CustomEvent

class FinalExtractor(IExtractElement[any]):    
    def extract(self, str_val: str, contract: SymboleoContract = None) -> any:
        return CustomEvent()
