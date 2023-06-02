from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.elements.obligation_subject import ObligationSubject
from app.src.selection.element_extractors.value_extractor import IExtractValue

class ObligationSubjectExtractor(IExtractValue[ObligationSubject]):
    def extract(self, str_val: str, contract: SymboleoContract = None) -> ObligationSubject:
        return ObligationSubject(str_val)
