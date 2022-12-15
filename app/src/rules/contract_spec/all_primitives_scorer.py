from typing import List, Dict
from app.classes.contract_update_request import ContractUpdateRequest
from app.classes.processing.scored_components import ScoredPrimitive
from app.src.component_identifiers.interfaces import IScorePrimitives

class IScoreAllPrimitives:
    def score(self, req: ContractUpdateRequest) -> List[ScoredPrimitive]:
        raise NotImplementedError()

class AllPrimitivesScorer(IScoreAllPrimitives):
    def __init__(
        self,
        identifier_dict: Dict[str, IScorePrimitives]
    ):
        self.__identifier_dict = identifier_dict
    
    def score(self, req: ContractUpdateRequest) -> List[ScoredPrimitive]:
        results = []

        for k in self.__identifier_dict:
            f = self.__identifier_dict[k]
            next_result = f.score(req)
            if next_result:
                results.append(next_result)
        
        return results