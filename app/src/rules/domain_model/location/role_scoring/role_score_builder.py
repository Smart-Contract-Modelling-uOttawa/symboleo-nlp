from typing import Dict, List
from app.classes.contract_update_request import ContractUpdateRequest

class IBuildRoleScores:
    def build(self, req: ContractUpdateRequest) -> Dict[str,float]:
        raise NotImplementedError()


class RoleScoreBuilder(IBuildRoleScores):
    def __init__(
        self,
        init_scores: Dict[str, float],
        inner_scorers: List[IBuildRoleScores]
    ):
        self.__init_scores = init_scores
        self.__inner_scorers = inner_scorers
    
    
    def build(self, req: ContractUpdateRequest) -> Dict[str,float]:
        # Create score dictionaries. Each one will return a dict of role scores
        # form will be {'seller': 0.4, 'buyer': 0.7}
        dicts = [x.build(req) for x in self.__inner_scorers]
        
        # Take the maximums
        result = {}
        for role in self.__init_scores:
            result[role] = max([x[role] for x in dicts])
        
        return result