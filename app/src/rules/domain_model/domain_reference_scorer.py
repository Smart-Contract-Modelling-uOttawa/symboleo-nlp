from typing import List, Tuple
from app.classes.domain_model.domain_model import DomainEvent
from app.classes.contract_update_request import ContractUpdateRequest
from app.src.rules.shared.interfaces import IScoreStuff
from app.src.rules.domain_model.property_similarity_scorer import IScoreProperySimilarity


class DomainReferenceScorer(IScoreStuff):
    def __init__(
        self,
        nlp,
        prop_name: str,
        property_similarity_scorer: IScoreProperySimilarity
    ):
        self.__nlp = nlp
        self.__prop_name = prop_name
        self.__prop_scorer = property_similarity_scorer


    def score(self, req: ContractUpdateRequest) -> List[Tuple[str, float]]:
        results = []

        # if we are referencing something in the domain
        ## Then we want to make use of it
        domain_events = req.contract.domain_model.events
        
        for evt in domain_events:
            d_evt = domain_events[evt]
            prop_match = [p for p in d_evt.props if self._sim_check(p.key, self.__prop_name)]
            if len(prop_match) == 0:
                continue
            
            evt_prop_scores = self._get_evt_prop_scores(d_evt, req.doc)
            sorted_scores = sorted(evt_prop_scores, key=lambda x: x[1], reverse=True)
            corrected_scores = [self._correct_score(score) for score in sorted_scores]
            top_score = corrected_scores[0]

            next_result = (f'{evt}.{self.__prop_name}', top_score[1])
            results.append(next_result)

        return results


        return super().score(req)


    def _correct_score(self, score):
        correction = 0.5
        return (score[0], score[1] + correction)


    def _get_evt_prop_scores(self, evt: DomainEvent, doc):
        results = []
        next_scores = self.__prop_scorer.get_scores(evt.props, doc)
            
        for ns in next_scores:
            results.append((f'{evt.name}.{ns}', next_scores[ns]))
        
        return results


    def _sim_check(self, s1, s2):
        d1 = self.__nlp(s1)
        d2 = self.__nlp(s2)

        return d1.similarity(d2) > 0.5 # set a threshold