from typing import List, Tuple, Dict
from app.classes.symboleo_contract import DomainEvent
from app.src.rules.domain_model.property_similarity_scorer import IScoreProperySimilarity

class IScoreDomainEventProps:
    def score(self, domain_events_dict: Dict[str, DomainEvent], doc) -> List[Tuple[str, float]]:
        raise NotImplementedError()


# Check if any domain events contain properties that match the request value 
class DomainEventPropScorer(IScoreDomainEventProps):
    def __init__(
        self,
        property_similarity_scorer: IScoreProperySimilarity,
        correction = 0
    ):
        self.__prop_scorer = property_similarity_scorer
        self.__correction = correction
    
    def score(self, domain_events_dict: Dict[str, DomainEvent], doc) -> List[Tuple[str, float]]:
        results = []
        
        for evt_key in domain_events_dict:
            evt = domain_events_dict[evt_key]
            next_scores = self.__prop_scorer.get_scores(evt.props, doc)

            # Convert to list and correct
            for ns in next_scores:
                results.append((f'{evt_key}.{ns}', next_scores[ns] + self.__correction))
        
        # Sort
        results = sorted(results, key=lambda x: x[1], reverse=True)

        return results



