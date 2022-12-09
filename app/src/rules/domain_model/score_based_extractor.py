from typing import List
from app.classes.contract_update_request import ContractUpdateRequest
from app.src.rules.shared.match_validator import IValidateMatches
from app.src.rules.shared.interfaces import IExtractProperties, IScoreStuff


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
        ## May be able to get rid of this one actually. 
        ## Push it to the scorers to send back messages
        self.__validator.validate(req.doc)

        # Iterate through scorers
        all_scores = []
        for scorer in self.__scorers:
            ## Want to handle situations where a scorer throws an error.
            ## We would wrap it in a catch, and log it in a message set - could be returned to user
            ## Will require a more sophsiticated output than a string. Thats fine!
            next_score_set = scorer.score(req)
            print(scorer.__class__, next_score_set)
            all_scores.extend(next_score_set)

        # Take the maximum score
        if len(all_scores) > 0:
            sorted_scores = sorted(all_scores, key=lambda x: x[1], reverse=True)
            print(sorted_scores)
            return sorted_scores[0][0]
        else:
            return None
    

