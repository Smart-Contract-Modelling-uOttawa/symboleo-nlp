from typing import List, Tuple
from app.classes.domain_model.domain_model import DomainProp
from app.classes.contract_update_request import ContractUpdateRequest
from app.src.rules.shared.interfaces import IScoreStuff
from app.src.rules.domain_model.location.role_score_builder import IBuildRoleScores
from app.src.rules.domain_model.property_similarity_scorer import IScoreProperySimilarity

class RoleScorer(IScoreStuff):
    def __init__(
        self, 
        nlp,
        role_score_builder: IBuildRoleScores,
        property_similarity_scorer: IScoreProperySimilarity
    ):
        self.__nlp = nlp
        self.__role_score_builder = role_score_builder
        self.__prop_scorer = property_similarity_scorer
    
    def score(self, req: ContractUpdateRequest) -> List[Tuple[str, float]]:
        results = []
        doc = req.doc
        domain_model = req.contract.domain_model

        # First build an updated role score dict based on keywords and coref
        role_score_dict = self.__role_score_builder.build(req)
    
        pieces = list(doc.noun_chunks) # Will be more sophisticated... addresses, noun_chunks, etc
        ## Want to treat addresses differently - requires an exact match...

        for role in role_score_dict:
            role_score = role_score_dict[role]
            role_props = domain_model.roles[role].props

            for p in pieces:
                # Have a better scoring mechanism
                p_score_dict = self.__prop_scorer.get_scores(role_props, p)

                for ps in p_score_dict:
                    next_score = p_score_dict[ps] * role_score
                    results.append((f'{role}.{ps}', next_score))
        
        return results
    