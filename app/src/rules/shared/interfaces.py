from typing import List, Tuple
from app.classes.symboleo_contract import SymboleoContract
from app.classes.contract_update_request import ContractUpdateRequest
from app.classes.contract_update_request import ContractUpdateRequest
from app.classes.spec.predicate_function import PredicateFunction
from app.classes.processing.scored_components import ScoredPredicate

class IScoreStuff:
    def score(self, req: ContractUpdateRequest) -> List[Tuple[str, float]]:
        raise NotImplementedError()


class IExtractProperties:
    def extract(self, req: ContractUpdateRequest) -> str:
        raise NotImplementedError()


class IBuildPropertyExtractor:
    @staticmethod
    def build(nlp) -> IExtractProperties:
        raise NotImplementedError()


class IExtractPredicates:
    def extract(self, req: ContractUpdateRequest) -> List[ScoredPredicate]:
        raise NotImplementedError()


class IBuildPredicateExtractor:
    @staticmethod
    def build(
        nlp, 
        template: PredicateFunction, 
        default_components = []
    ) -> IExtractPredicates:
        raise NotImplementedError()


class IProcessDocs:
    def process(self, req: ContractUpdateRequest) -> SymboleoContract:
        raise NotImplementedError()
