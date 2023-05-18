from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.template_event.obligation_subject import ObligationSubject
from app.src.extractors.value_extractor import IExtractValue

# This is where we may want to add the contract in
## For example, to verify that it's a legitimate obligation 
class ObligationSubjectExtractor(IExtractValue[ObligationSubject]):
    def extract(self, str_val: str, contract: SymboleoContract = None) -> ObligationSubject:
        return ObligationSubject(str_val)
