from typing import List, Tuple
from app.classes.contract_update_request import ContractUpdateRequest
from app.src.rules.shared.interfaces import IScoreStuff
from app.src.rules.domain_model.location.role_scoring.role_score_builder import IBuildRoleScores
from app.src.rules.domain_model.location.location_span_extractor import IExractLocationSpans
from app.src.rules.domain_model.location.role_scoring.role_score_assembler import IAssembleRoleScores

class RoleScorer(IScoreStuff):
    def __init__(
        self,
        location_span_extractor: IExractLocationSpans,
        role_score_builder: IBuildRoleScores,
        role_score_assembler: IAssembleRoleScores
    ):
        self.__location_span_extractor = location_span_extractor
        self.__role_score_builder = role_score_builder
        self.__role_score_assembler = role_score_assembler


    # e.g. result [('buyer.some_prop', 0.8), ('seller.another_prop', 0.4)]
    def score(self, req: ContractUpdateRequest) -> List[Tuple[str, float]]:
        location = self.__location_span_extractor.extract(req.doc)
        if location is None:
            return []

        role_score_dict = self.__role_score_builder.build(req)

        results = self.__role_score_assembler.assemble(role_score_dict, req.contract.domain_model, location)

        return results

    
    # May want to frame this to be a function of a few things
    ## score(role) = F(bias, role_score, prop_score)
    ## a0: bias <- input from config
    ## a1: role_score <- max of role_coref_dict and role_match_dict
    ## a2: prop_score <- get max prop from key/value similarities for the best-matching prop
    # Then the score is going to be score = F(a0, a1, a2). Can do average, harmonic, sum, max, etc. 
    # We can get a list of scores, or even a tensor, then take the max as well, or do thresholds  

    

     