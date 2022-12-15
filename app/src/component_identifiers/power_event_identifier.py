from app.classes.processing.scored_components import ScoredPrimitive
from app.src.component_identifiers.interfaces import IScorePrimitives
from app.src.matcher_helper import IGetMatches

from app.classes.spec.sym_event import PowerEvent
from app.src.component_identifiers.helpers.event_scorer import IScoreEvents
from app.src.component_identifiers.helpers.variable_scorer import IScoreVariables

class PowerEventIdentifier(IScorePrimitives):
    def __init__(
        self, 
        event_name_scorer: IScoreEvents, 
        variable_scorer: IScoreVariables
    ):
        self.__event_name_scorer = event_name_scorer
        self.__variable_scorer = variable_scorer


    def identify(self, doc) -> ScoredPrimitive:
        event_name, event_score = self.__event_name_scorer.score(doc)

        variable, var_score = self.__variable_scorer.score(doc)

        score = round(event_score * var_score, 3)

        primitive = PowerEvent(event_name, variable)

        return ScoredPrimitive(primitive, score)
    
