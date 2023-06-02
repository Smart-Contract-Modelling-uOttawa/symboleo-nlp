from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.events.custom_event.noun_phrase import NounPhrase
from app.classes.events.template_event.contract_components import ContractNouns
from app.src.selection.element_extractors.value_extractor import IExtractValue

class ContractSubjectExtractor(IExtractValue[NounPhrase]):    
    def extract(self, str_val: str, contract: SymboleoContract = None) -> NounPhrase:
        return ContractNouns.contract()
