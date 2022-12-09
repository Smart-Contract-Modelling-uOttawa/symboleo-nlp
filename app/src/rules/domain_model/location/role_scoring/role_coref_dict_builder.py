import copy
import re
from typing import Dict
from app.src.rules.domain_model.location.role_scoring.role_score_builder import IBuildRoleScores
from app.src.rules.domain_model.location.coref_getter import IGetCorefs
from app.src.rules.domain_model.location.role_scoring.coref_template_prepper import IPrepCorefTemplates
from app.classes.contract_update_request import ContractUpdateRequest

# Checks if a doc matches a list of roles verbatim
class RoleCorefDictBuilder(IBuildRoleScores):
    def __init__(
        self,
        init_scores: Dict[str, float],
        coref_prepper: IPrepCorefTemplates,
        coref_getter: IGetCorefs
    ):
        self.__init_scores = init_scores
        self.__coref_prepper = coref_prepper
        self.__coref_getter = coref_getter
        self.__coref_match_score = 0.9 # May pass this in


    def build(self, req: ContractUpdateRequest) -> Dict[str, float]:
        result = copy.deepcopy(self.__init_scores)

        # Corefs 
        full_doc, base_index = self.__coref_prepper.prep(req)
        
        # Result of this will be a dict. 
        ## key: doc index of the coref (we dont care about this)
        ## value: list of strings that are part of the coref set
        coref_set = self.__coref_getter.get(req.doc, base_index, full_doc)
        
        # Look for the roles in each of the coref sets
        for cr in coref_set:
            corefs = coref_set[cr] # list of strings
            for c in corefs:
                if c in result:
                    result[c] = self.__coref_match_score
        
        return result


    