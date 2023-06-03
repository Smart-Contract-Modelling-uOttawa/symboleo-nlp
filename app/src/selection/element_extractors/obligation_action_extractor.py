from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.sym_event import ObligationEventName
from app.src.selection.element_extractors.element_extractor import IExtractElement

class ObligationActionExtractor(IExtractElement[ObligationEventName]):    
    def extract(self, str_val: str, contract: SymboleoContract = None) -> ObligationEventName:
        return ObligationEventName[str_val.capitalize()]
