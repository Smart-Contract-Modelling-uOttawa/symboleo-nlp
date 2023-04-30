from typing import List
from app.classes.custom_event.custom_event import CustomEvent
from app.classes.custom_event.noun_phrase import NounPhrase
from app.classes.custom_event.verb import Verb, VerbType, VerbConjugations
from app.classes.custom_event.adverb import Adverb
from app.classes.custom_event.predicate import Predicate
from app.classes.custom_event.prep_phrase import PrepPhrase

class CommonEvent(CustomEvent):
    def __init__(
            self, 
            subj: NounPhrase = None, 
            verb: Verb = None, 
            adverb: Adverb = None, 
            dobj: NounPhrase = None, 
            predicate: Predicate = None, 
            pps: List[PrepPhrase] = None,
            common_event_key: str = ''
        ):
        super().__init__(subj, verb, adverb, dobj, predicate, pps)
        self.common_event_key = common_event_key
