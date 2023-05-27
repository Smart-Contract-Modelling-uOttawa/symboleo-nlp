from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.custom_event.noun_phrase import NounPhrase
from app.classes.template_event.contract_components import ContractNouns
from app.src.extractors.value_extractor import IExtractValue

class ContractSubjectExtractor(IExtractValue[NounPhrase]):    
    def extract(self, str_val: str, contract: SymboleoContract = None) -> NounPhrase:
        return ContractNouns.contract()
