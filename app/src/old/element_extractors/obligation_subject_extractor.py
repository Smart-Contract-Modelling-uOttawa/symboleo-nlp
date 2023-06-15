from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.elements.obligation_subject import ObligationSubject
from app.src.element_extractors.element_extractor import IExtractElement

class ObligationSubjectExtractor(IExtractElement[ObligationSubject]):
    def extract(self, str_val: str, contract: SymboleoContract = None) -> ObligationSubject:
        return ObligationSubject(str_val)
