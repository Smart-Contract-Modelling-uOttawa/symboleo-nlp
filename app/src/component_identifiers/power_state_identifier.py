from app.classes.processing.scored_components import ScoredPrimitive
from app.src.component_identifiers.interfaces import IScorePrimitives
from app.src.matcher_helper import IGetMatches

from app.classes.spec.sym_situation import PowerState
from app.src.component_identifiers.helpers.state_name_scorer import IScoreStates
from app.src.component_identifiers.helpers.variable_scorer import IScoreVariables

class PowerStateIdentifier(IScorePrimitives):
    def __init__(
        self, 
        state_name_scorer: IScoreStates, 
        power_scorer: IScoreVariables
    ):
        self.__state_name_scorer = state_name_scorer
        self.__power_scorer = power_scorer


    def identify(self, doc) -> ScoredPrimitive:
        state_name, state_score = self.__state_name_scorer.score(doc)

        power_variable, var_score = self.__power_scorer.score(doc)

        score = round(state_score * var_score, 3)

        primitive = PowerState(state_name, power_variable)

        return ScoredPrimitive(primitive, score)
    
