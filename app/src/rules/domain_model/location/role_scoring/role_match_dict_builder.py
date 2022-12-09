import copy
from typing import Dict
from app.classes.contract_update_request import ContractUpdateRequest
from app.src.rules.domain_model.location.role_scoring.role_score_builder import IBuildRoleScores
from app.src.matcher_helper import IGetMatches
from app.src.rules.domain_model.location.role_scoring.role_pattern_builder import IBuildRolePatterns

# Checks if a doc matches a list of roles verbatim
class RoleMatchDictBuilder(IBuildRoleScores):
    def __init__(
        self,
        init_scores: Dict[str, float],
        pattern_builder: IBuildRolePatterns,
        matcher: IGetMatches
    ):
        self.__init_scores = init_scores
        self.__pattern_builder = pattern_builder
        self.__matcher = matcher
    

    def build(self, req: ContractUpdateRequest):
        result = copy.deepcopy(self.__init_scores)

        for role_name in result:
            pattern = self.__pattern_builder.build(role_name)
            role_match = self.__matcher.match(pattern, req.doc)
            if role_match:
                result[role_name] = 1
        
        return result

    