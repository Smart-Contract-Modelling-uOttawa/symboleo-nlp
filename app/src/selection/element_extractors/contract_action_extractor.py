from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.sym_event import ContractEventName
from app.src.selection.element_extractors.value_extractor import IExtractValue

class ContractActionExtractor(IExtractValue[ContractEventName]):    
    def extract(self, str_val: str, contract: SymboleoContract = None) -> ContractEventName:
        return ContractEventName[str_val.capitalize()]
