from app.classes.symboleo_contract import SymboleoContract

class ContractUpdateRequest:
    def __init__(self, contract: SymboleoContract, key: str, value: str, doc):
        self.contract = contract
        self.key = key
        self.value = value
        self.doc = doc