from app.src.matcher_helper import IGetMatches
from app.classes.spec.sym_event import EventVDE
from app.classes.spec.primitive import ScoredPrimitive
from app.src.primitive_identifiers.primitive_identifier import IIdentifyPrimitives

class EventVdeIdentifier(IIdentifyPrimitives):
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
            return ScoredPrimitive(EventVDE(match.text), 1)
        
        return None

