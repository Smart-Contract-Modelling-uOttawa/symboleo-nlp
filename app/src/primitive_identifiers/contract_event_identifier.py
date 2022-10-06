from app.classes.spec.primitive import ScoredPrimitive
from app.classes.spec.sym_event import ContractEvent
from app.src.primitive_identifiers.event_scorer import IScoreEvents
from app.src.primitive_identifiers.primitive_identifier import IIdentifyPrimitives

class ContractEventIdentifier(IIdentifyPrimitives):
    def __init__(
        self, 
        event_name_scorer: IScoreEvents
    ):
        self.__event_name_scorer = event_name_scorer

    # TODO: Will need some more attention, since there is no variable
    ## May look for other hints, such as the presence of word contract
    def identify(self, doc) -> ScoredPrimitive:
        event_name, event_score = self.__event_name_scorer.score(doc)

        score = round(event_score * 0.7, 3)

        primitive = ContractEvent(event_name)

        return ScoredPrimitive(primitive, score)
    
