from typing import Dict, List, Tuple
from app.classes.symboleo_contract import DomainModel
from spacy.tokens.span import Span
from app.src.rules.domain_model.property_similarity_scorer import IScoreProperySimilarity

class IAssembleRoleScores:
    def assemble(
        self, 
        role_score_dict: Dict[str, float],
        domain_model: DomainModel,
        location: Span
    ) -> List[Tuple[str, float]]:
        raise NotImplementedError()


class RoleScoreAssembler(IAssembleRoleScores):
    def __init__(self, prop_scorer: IScoreProperySimilarity):
        self.__prop_scorer = prop_scorer

    def assemble(self, role_score_dict: Dict[str, float], domain_model: DomainModel, location: Span) -> List[Tuple[str, float]]:
        results = []

        print('rsd', role_score_dict)
        
        for role in role_score_dict: 
            role_props = domain_model.roles[role].props
            p_score_dict = self.__prop_scorer.get_scores(role_props, location)
            role_score = role_score_dict[role]
            print('ps', role, p_score_dict)
            
            for ps in p_score_dict:
                next_score = p_score_dict[ps] * role_score
                results.append((f'{role}.{ps}', next_score))

        return results