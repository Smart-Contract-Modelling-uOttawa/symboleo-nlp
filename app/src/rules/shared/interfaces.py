from typing import List, Tuple
from app.classes.symboleo_contract import SymboleoContract
from app.classes.contract_update_request import ContractUpdateRequest
from app.classes.contract_update_request import ContractUpdateRequest


class IScoreStuff:
    def score(self, req: ContractUpdateRequest) -> List[Tuple[str, float]]:
        raise NotImplementedError()


class IExtractProperties:
    def extract(self, req: ContractUpdateRequest) -> str:
        raise NotImplementedError()


class IExtractPredicates:
    def extract(self, req: ContractUpdateRequest):
        raise NotImplementedError()


class IProcessDocs:
    def process(self, req: ContractUpdateRequest) -> SymboleoContract:
        raise NotImplementedError()
