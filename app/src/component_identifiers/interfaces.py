from app.classes.contract_update_request import ContractUpdateRequest
from app.classes.processing.scored_components import ScoredPrimitive

class IScorePrimitives:
    def score(self, req: ContractUpdateRequest) -> ScoredPrimitive:
        raise NotImplementedError()