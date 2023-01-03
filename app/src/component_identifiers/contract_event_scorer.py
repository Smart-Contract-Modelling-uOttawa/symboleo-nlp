from app.classes.processing.scored_components import ScoredPrimitive
from app.src.component_identifiers.interfaces import IScorePrimitives
from app.src.matcher_helper import IGetMatches
from app.classes.spec.sym_event import ContractEvent
from app.src.component_identifiers.helpers.event_scorer import IScoreEvents


class ContractEventScorer(IScorePrimitives):
    def __init__(
        self, 
        event_name_scorer: IScoreEvents
    ):
        self.__event_name_scorer = event_name_scorer

    # TODO: Will need some more attention, since there is no variable
    ## May look for other hints, such as the presence of word contract
    def score(self, doc) -> ScoredPrimitive:
        # START HERE!!
        # Lots of wordnet

        # Steps
        ## look for a noun that suggests a contract
        ## If found, look for a relation to a relevant contract-related verb
        ## etc etc etc
        return None

        event_name, event_score = self.__event_name_scorer.score(doc)

        score = round(event_score * 0.7, 3)

        primitive = ContractEvent(event_name)

        return ScoredPrimitive(primitive, score)
    
