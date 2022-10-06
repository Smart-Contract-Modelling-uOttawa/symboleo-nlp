from app.classes.spec.primitive import ScoredPrimitive
from app.classes.spec.sym_situation import ObligationState
from app.src.primitive_identifiers.primitive_identifier import IIdentifyPrimitives
from app.src.primitive_identifiers.state_name_scorer import IScoreStates
from app.src.primitive_identifiers.variable_scorer import IScoreVariables

class ObligationStateIdentifier(IIdentifyPrimitives):
    def __init__(
        self, 
        state_name_scorer: IScoreStates, 
        obligation_scorer: IScoreVariables
    ):
        self.__state_name_scorer = state_name_scorer
        self.__obligation_scorer = obligation_scorer


    def identify(self, doc) -> ScoredPrimitive:
        state_name, state_score = self.__state_name_scorer.score(doc)

        obligation_variable, ob_score = self.__obligation_scorer.score(doc)

        score = round(state_score * ob_score, 3)

        primitive = ObligationState(state_name, obligation_variable)

        return ScoredPrimitive(primitive, score)
    
