from app.classes.processing.scored_components import ScoredPrimitive
from app.src.component_identifiers.interfaces import IScorePrimitives
from app.src.matcher_helper import IGetMatches
from app.classes.spec.sym_event import VariableEvent

class VariableEventIdentifier(IScorePrimitives):
    def __init__(
        self,
        matcher: IGetMatches
    ):
        self.__matcher = matcher

    def identify(self, doc) -> ScoredPrimitive:
        # Want this to mainly look for events from the domain model...
        pattern = [
            [{"POS": "NOUN", "ENT_TYPE": "DOMAIN_EVENT" }],
        ]
        match = self.__matcher.match(pattern, doc)

        if match:
            return ScoredPrimitive(VariableEvent(match.text), 1)
        
        return None

