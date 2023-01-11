from typing import List
from app.classes.contract_update_request import ContractUpdateRequest
from app.src.rules.shared.interfaces import IExtractPredicates
from app.classes.processing.scored_components import ScoredPredicate, ScoredParameter
from app.src.rules.contract_spec.predicate_scorer import IScorePredicates
from app.src.rules.contract_spec.parameter_scorer import IScoreParameters
from app.src.rules.contract_spec.pred_parm_combiner import ICombinePredsParms

# Might rename...
class PredicateExtractor(IExtractPredicates):
    def __init__(
        self, 
        predicate_scorer: IScorePredicates,
        parameter_scorer: IScoreParameters,
        combiner: ICombinePredsParms
    ):
        self.__predicate_scorer = predicate_scorer
        self.__parameter_scorer = parameter_scorer
        self.__combiner = combiner

    def extract(self, req: ContractUpdateRequest) -> List[ScoredPredicate]: 
        preds = self.__predicate_scorer.score(req)

        if len(preds) == 0:
            return []  

        parms = self.__parameter_scorer.score(req)
        self._print_parms(parms)
        if len(parms) == 0:
            return []

        result_set = self.__combiner.combine(preds, parms)

        return result_set
    

    def _print_parms(self, parms: List[ScoredParameter]):
        print('\nPARMS:')
        for x in parms:
            print('--', x.obj.to_sym(), x.score)
        print('\n')
