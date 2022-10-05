from app.classes.spec.primitive import ScoredPrimitive
from app.classes.spec.sym_event import ObligationEvent
from app.src.primitive_identifiers.event_scorer import IScoreEvents
from app.src.primitive_identifiers.primitive_identifier import IIdentifyPrimitives
from app.src.primitive_identifiers.variable_scorer import IScoreVariables

class ObligationEventIdentifier(IIdentifyPrimitives):
    def __init__(
        self, 
        event_name_scorer: IScoreEvents, 
        obligation_scorer: IScoreVariables
    ):
        self.__event_name_scorer = event_name_scorer
        self.__obligation_scorer = obligation_scorer


    def identify(self, doc) -> ScoredPrimitive:
        event_name, event_score = self.__event_name_scorer.score(doc)

        obligation_variable, ob_score = self.__obligation_scorer.score(doc)

        score = round(event_score * ob_score, 3)

        primitive = ObligationEvent(event_name, obligation_variable)

        return ScoredPrimitive(primitive, score)
    
