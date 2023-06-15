from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.events.custom_event.noun_phrase import NounPhrase
from app.classes.events.template_event.contract_components import ContractNouns
from app.src.element_extractors.element_extractor import IExtractElement

class ContractSubjectExtractor(IExtractElement[NounPhrase]):    
    def extract(self, str_val: str, contract: SymboleoContract = None) -> NounPhrase:
        return ContractNouns.contract()
