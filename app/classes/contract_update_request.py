from app.classes.symboleo_contract import SymboleoContract
from spacy.tokens.doc import Doc

class ContractUpdateRequest:
    def __init__(self, contract: SymboleoContract, key: str, value: str, doc:Doc):
        self.contract = contract
        self.key = key
        self.value = value
        self.doc = doc