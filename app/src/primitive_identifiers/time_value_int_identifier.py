from app.classes.spec.helpers import TimeValueInt
from app.classes.spec.primitive import ScoredPrimitive
from app.src.primitive_identifiers.primitive_identifier import IIdentifyPrimitives

class TimeValueIntIdentifier(IIdentifyPrimitives):
    def __init__(
        self, 
    ):
        self.s = 0

    # TODO: Should likely focus on spacy "entities" here
    # TODO: May also want to convert anything to actual numbers
    def identify(self, doc) -> ScoredPrimitive:
        # Look for numbers that are close to time units?
        target1 = [x for x in doc if x.dep_ == 'nummod' and x.ent_type_ in ['TIME', 'DATE']]

        target2 = [x for x in doc if x.dep_ == 'nummod']

        target3 = [x for x in doc if x.pos_ == 'NUM']

        if len(target1) > 0:
            primitive = TimeValueInt(target1[0].text)
            score = 1
        elif len(target2) > 0:
            primitive = TimeValueInt(target2[0].text)
            score = 0.7
        elif len(target3) > 0:
            primitive = TimeValueInt(target3[0].text)
            score = 0.2
        else:
            primitive = TimeValueInt(0)
            score = 0

        return ScoredPrimitive(primitive, score)
    
