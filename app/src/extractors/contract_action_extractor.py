from app.classes.spec.sym_event import ContractEventName

# TODO: These need to inherit from the extractor interface
class ContractActionExtractor:    
    def extract(self, str_val: str) -> ContractEventName:
        return ContractEventName[str_val.capitalize()]
