from __future__ import annotations
from typing import List
from app.classes.custom_event.conj_type import ConjType

from app.classes.custom_event.noun_phrase import NounPhrase
from app.classes.custom_event.verb import Verb, VerbType
from app.classes.custom_event.predicate import Predicate
from app.classes.custom_event.adverb import Adverb
from app.classes.custom_event.prep_phrase import PrepPhrase

from app.classes.other.helpers import ClassHelpers

class CustomEvent:
    subj: NounPhrase = None
    verb: Verb = None
    adverb: Adverb = None
    dobj: NounPhrase = None
    predicate: Predicate = None
    pps: List[PrepPhrase] = None

    def __init__(self, subj: NounPhrase = None, verb: Verb = None, adverb: Adverb = None, dobj: NounPhrase = None, predicate: Predicate = None, pps:List[PrepPhrase] = None):
        self.subj = subj
        self.verb = verb
        self.adverb = adverb
        self.dobj = dobj
        self.predicate = predicate
        self.pps = pps

    # TODO: This will be more complex. Will need to split it out, potentially into static functions. Need tests
    def to_text(self, conjugation: ConjType = ConjType.PRESENT):
        result = ''

        subj = self.subj.to_text()

        if conjugation == ConjType.PRESENT:
            if self.subj.is_plural:
                verb = self.verb.conjugations.present_singular
            else:
                verb = self.verb.conjugations.present_plural
        elif conjugation == ConjType.CONTINUOUS:
            verb = self.verb.conjugations.continuous

        if self.dobj and VerbType.TRANSITIVE in self.verb.verb_types:
            dobj = self.dobj.to_text()
            result = f'{subj} {verb} {dobj}'

        elif VerbType.INTRANSITIVE in self.verb.verb_types:
            result = f'{subj} {verb}'
        
        elif VerbType.LINKING in self.verb.verb_types:
            if self.subj.is_plural:
                verb = self.verb.conjugations.present_plural
            else:
                verb = self.verb.conjugations.present_singular
            
            if self.predicate:
                pred = self.predicate.to_text()
                result = f'{subj} {verb} {pred}'
            
        if self.adverb:
            adverb = self.adverb.to_text()
            result = f'{result} {adverb}'
        
        if self.pps:
            for pp in self.pps:
                result = f'{result} {pp.to_text()}'

        return result

    def __eq__(self, other: CustomEvent) -> bool:
        return self.subj == other.subj and \
            self.dobj == other.dobj and \
            self.verb == other.verb and \
            self.adverb == other.adverb and \
            self.predicate == other.predicate and \
            ClassHelpers.lists_eq(self.pps, other.pps, 'key')

    # TODO: Make this more complex
    def is_complete(self):
        return self.subj and self.verb

