from app.src.matcher_helper import IGetMatches
from app.classes.spec.primitive import ScoredPrimitive
from app.classes.spec.sym_event import ObligationEvent
from app.src.primitive_identifiers.event_scorer import IScoreEvents
from app.src.primitive_identifiers.primitive_identifier import IIdentifyPrimitives
from app.src.primitive_identifiers.variable_scorer import IScoreVariables

class ObligationEventIdentifier(IIdentifyPrimitives):
    def __init__(
        self,
        matcher: IGetMatches
    ):
        self.__matcher = matcher
        # self.__event_name_scorer = event_name_scorer
        # self.__obligation_scorer = obligation_scorer

    # TODO: I may want to actually split the ObligationEvent up into separate string primitives...
    # defn of primitive may need to just be a single token/span/argument
    def identify(self, doc) -> ScoredPrimitive:
        # This needs to be populated from the domain_model or contract spec.
        # Likely needs to be pre-init'd and passed in separately
        # Look at the identify_old ideas - probably revive them a little
        obligation_variable_pattern = [
            [{"LOWER": {"IN": ['payment', 'delivery'] }}],
        ]
        ov_match = self.__matcher.match(obligation_variable_pattern, doc)

        # payment not made => Violated
        negation_pattern = [
            [{'LOWER': 'not'}, {'POS': 'VERB'}]
        ]
        neg_match = self.__matcher.match(negation_pattern, doc)

        if ov_match and neg_match:
            primitive = ObligationEvent('Violated', ov_match.text)

            return ScoredPrimitive(primitive, 1)
        
        return None


    def identify_old(self, doc) -> ScoredPrimitive:
        event_name, event_score = self.__event_name_scorer.score(doc)

        obligation_variable, ob_score = self.__obligation_scorer.score(doc)

        score = round(event_score * ob_score, 3)

        primitive = ObligationEvent(event_name, obligation_variable)

        return ScoredPrimitive(primitive, score)
    
