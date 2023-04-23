from app.classes.spec.sym_event import ObligationEventName
from app.src.extractors.value_extractor import IExtractValue

class ObligationActionExtractor(IExtractValue[ObligationEventName]):    
    def extract(self, str_val: str) -> ObligationEventName:
        return ObligationEventName[str_val.capitalize()]
