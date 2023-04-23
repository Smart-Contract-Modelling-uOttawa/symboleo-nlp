from app.classes.spec.sym_event import ContractEventName
from app.src.extractors.value_extractor import IExtractValue

# TODO: These need to inherit from the extractor interface
class ContractActionExtractor(IExtractValue[ContractEventName]):    
    def extract(self, str_val: str) -> ContractEventName:
        return ContractEventName[str_val.capitalize()]
