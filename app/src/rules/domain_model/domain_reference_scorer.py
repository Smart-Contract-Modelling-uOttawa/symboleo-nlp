from typing import List, Tuple, Dict
from app.classes.domain_model.domain_model import DomainEvent
from app.classes.contract_update_request import ContractUpdateRequest
from app.src.rules.shared.interfaces import IScoreStuff
from app.src.rules.domain_model.domain_event_prop_scorer import IScoreDomainEventProps

# Given a target property, we want to check the events in the domain model to see 
# if the request value is making reference to it
class DomainReferenceScorer(IScoreStuff):
    def __init__(
        self,
        nlp,
        prop_name: str,
        domain_event_prop_scorer: IScoreDomainEventProps
    ):
        self.__nlp = nlp
        self.__prop_name = prop_name # Instead of this, may treat it like a filterer. Prop name, type, etc.?
        self.__domain_event_prop_scorer = domain_event_prop_scorer


    def score(self, req: ContractUpdateRequest) -> List[Tuple[str, float]]:     
        # Filter the events to those that contain a matching property (pull this out)
        filtered_events = self._filter_events(req.contract.domain_model.events)
        
        # Get the scores on the filtered events
        results = self.__domain_event_prop_scorer.score(filtered_events, req.doc)
        
        return results


    # TODO: Should pull this out
    def _filter_events(self, domain_events: Dict[str, DomainEvent]):
        # May make this a more generic filtering mechanism?
        filtered_events = {}
        for evt_key in domain_events:
            d_evt = domain_events[evt_key]
            prop_match = [p for p in d_evt.props if self._sim_check(p.key, self.__prop_name)]
            if len(prop_match) > 0:
                filtered_events[evt_key] = d_evt

    # This will probably change as well...
    def _sim_check(self, s1, s2):
        d1 = self.__nlp(s1)
        d2 = self.__nlp(s2)

        return d1.similarity(d2) > 0.5 # set a threshold