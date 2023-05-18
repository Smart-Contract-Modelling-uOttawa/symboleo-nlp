from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.sym_event import ObligationEventName
from app.src.extractors.value_extractor import IExtractValue

class ObligationActionExtractor(IExtractValue[ObligationEventName]):    
    def extract(self, str_val: str, contract: SymboleoContract = None) -> ObligationEventName:
        return ObligationEventName[str_val.capitalize()]
