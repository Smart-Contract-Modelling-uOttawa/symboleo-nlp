from typing import List
from app.src.rules.contract_spec.dynamic_constructor import IConstructDynamicObjects
from app.classes.processing.scored_components import ScoredPredicateType, ScoredPredicate, ScoredParameter

# Given a set of predicate types and parameters, combine them to make a full predicate
class ICombinePredsParms:
    def combine(self, scored_preds: List[ScoredPredicateType], scored_parms: List[ScoredParameter]) -> List[ScoredPredicate]:
        raise NotImplementedError


class PredParmCombiner(ICombinePredsParms):
    def __init__(
        self, 
        dynamic_constructor: IConstructDynamicObjects
    ):
        self.__dynamic_constructor = dynamic_constructor

    def combine(self, scored_preds: List[ScoredPredicateType], scored_parms: List[ScoredParameter]) -> List[ScoredPredicate]:
        results = []

        for sp in scored_preds:
            fp = self.__dynamic_constructor.construct(sp, scored_parms)
            if fp:
                next_predicate = ScoredPredicate(fp.obj, fp.score)
                results.append(next_predicate)

        return results