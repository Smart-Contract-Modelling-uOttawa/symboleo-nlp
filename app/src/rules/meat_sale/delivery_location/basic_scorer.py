from typing import List, Tuple
from app.classes.contract_update_request import ContractUpdateRequest
from app.src.rules.shared.interfaces import IScoreStuff

class BasicScorer(IScoreStuff):
    def __init__(
        self, 
        default_value: str,
        default_score: float = 0
    ):
        self.__default_value = default_value
        self.__default_score = default_score
    
    def score(self, req: ContractUpdateRequest) -> List[Tuple[str, float]]:
        return [(self.__default_value, self.__default_score)] 
