from app.classes.spec.primitive import ScoredPrimitive
from app.classes.spec.sym_situation import ContractState
from app.src.primitive_identifiers.primitive_identifier import IIdentifyPrimitives
from app.src.primitive_identifiers.state_name_scorer import IScoreStates

class ContractStateIdentifier(IIdentifyPrimitives):
    def __init__(
        self, 
        state_name_scorer: IScoreStates
    ):
        self.__state_name_scorer = state_name_scorer

    # TODO: Need another way to identify contract events/states - e.g. look for the term "agreement"...
    def identify(self, doc) -> ScoredPrimitive:
        state_name, state_score = self.__state_name_scorer.score(doc)

        score = round(state_score * 0.7, 3)

        primitive = ContractState(state_name)

        return ScoredPrimitive(primitive, score)
    
