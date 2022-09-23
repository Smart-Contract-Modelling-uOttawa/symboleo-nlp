from app.classes.spec.atoms import SituationProposition
from app.classes.spec.helpers import Interval, Situation
from app.lib.matchers.interfaces import IMatcher, IValidateMatches
from app.classes.spec.symboleo_spec import NegAtom

# Very simple matcher: "the sky is blue"
class SimpleMatcher(IMatcher):
    def __init__(
        self, 
        key,
        nlp,
        validator
    ):
        self.__key: str = key
        self.__nlp = nlp
        self.__validator: IValidateMatches = validator
    
    def key(self):
        return self.__key
    
    def try_match(self, doc) -> NegAtom:
        if not self.__validator.validate(doc):
            return None

        # Parsing stage
        verb = [x for x in doc if x.tag_ == 'VBZ'][0].text
        adj = [x for x in doc if x.tag_ == 'JJ'][0].text
        subj = [x for x in doc if x.tag_ == 'NN'][0].text

        #pred_spec = SimplePredSpec(verb, adj, subj) ## May bring back something like this...
        situation_name = f'{verb}_{adj}({subj})'

        return NegAtom(
            SituationProposition(
                Situation(situation_name),
                Interval('X')
            )
        )
