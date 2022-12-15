from typing import List
from app.classes.contract_update_request import ContractUpdateRequest
from app.classes.processing.scored_components import ScoredPredicateType
from app.classes.processing.case_obj import CasePattern
from app.src.matcher_helper import IGetMatches

# Find the most likely predicates for an input
# May need the whole req, since we want context as well
class IScorePredicates:
    def score(self, req: ContractUpdateRequest) -> List[ScoredPredicateType]:
        raise NotImplementedError()


class PredicateScorer(IScorePredicates):
    def __init__(
        self,
        case_patterns: List[CasePattern],
        matcher: IGetMatches
    ):
        self.__case_patterns = case_patterns # key, pattern, Pred
        self.__matcher = matcher
    

    def score(self, req: ContractUpdateRequest) -> List[ScoredPredicateType]:
        # We have a finite set of predicates.
        # Need to choose the most likely 
        # Ideas: Spacy Patterns, template (some sort of refinement map) 
        # This can be an assembly of different functions. For now, keep it simple and structured. 
        ## Can later add other ones in
        ## May turn it into another scoring aggregator... 
        results = []

        for x in self.__case_patterns:
            try_case = self.__matcher.match(x.pattern, req.doc)
            if try_case:
                next_score = 1 # Change this?
                next_result = ScoredPredicateType(x.pred, next_score)
                results.append(next_result)

        return results
    

