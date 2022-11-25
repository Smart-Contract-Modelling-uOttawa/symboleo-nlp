from typing import List
from app.classes.contract_update_request import ContractUpdateRequest
from app.src.rules.shared.match_validator import IValidateMatches
from app.src.rules.shared.interfaces import IExtractProperties, IScoreStuff

# This is the exact same as location_extractor.
## May be able to collapse them into one thing... score_based_extractor?
## This is just extracting a single property
## So we need to separate the currency and the score... Would like to have some coherence though...

class ScoreBasedExtractor(IExtractProperties):
    def __init__(
        self,
        nlp,
        validator: IValidateMatches,
        scorers: List[IScoreStuff]
    ):
        self.__nlp = nlp
        self.__validator = validator
        self.__scorers = scorers

    
    def extract(self, req: ContractUpdateRequest) -> str:
        # Initial validation
        self.__validator.validate(req.doc)

        # Iterate through scorers
        all_scores = []
        for scorer in self.__scorers:
            next_score_set = scorer.score(req)
            all_scores.extend(next_score_set)

        # Take the maximum score
        if len(all_scores) > 0:
            sorted_scores = sorted(all_scores, key=lambda x: x[1], reverse=True)
            print(sorted_scores)
            return sorted_scores[0][0]
        else:
            return None
    
