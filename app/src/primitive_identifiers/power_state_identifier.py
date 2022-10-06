from app.classes.spec.primitive import ScoredPrimitive
from app.classes.spec.sym_situation import PowerState
from app.src.primitive_identifiers.primitive_identifier import IIdentifyPrimitives
from app.src.primitive_identifiers.state_name_scorer import IScoreStates
from app.src.primitive_identifiers.variable_scorer import IScoreVariables

class PowerStateIdentifier(IIdentifyPrimitives):
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
    
