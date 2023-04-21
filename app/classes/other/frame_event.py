from __future__ import annotations
from typing import List
from enum import Enum
from app.classes.other.noun_phrase import NounPhrase
from app.classes.other.verb import Verb, VerbType
from app.classes.other.predicate import Predicate
from app.classes.other.adverb import Adverb
from app.classes.other.prep_phrase import PrepPhrase

class ConjType(Enum):
    PRESENT = 'present',
    CONTINUOUS = 'continuous'


# TODO: Going to be spending LOTS of time on this...
## Will address each of the components
## Subj and Dobj might use the same thing
## Likely won't do much for predicate
## PPs will be a bit tougher. Will split out the first word, ensure it conforms to prep, etc

class FrameEvent:
    # Add types to all of these
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


    # Will likely be passing in conjugation information (maybe a conjugation type)
    # Might even get a few results...
    # Conjugations 
    ## within 2 weeks  of X being evented(past)
    # Might be a static function. It's pretty long
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

        if VerbType.TRANSITIVE in self.verb.verb_types:
            if self.dobj:
                dobj = self.dobj.to_text()
                result = f'{subj} {verb} {dobj}'
        
        if VerbType.INTRANSITIVE in self.verb.verb_types:
            result = f'{subj} {verb}'
        
        if VerbType.LINKING in self.verb.verb_types:
            if self.predicate:
                pred = self.predicate.to_text()
                result = f'{subj} {verb} {pred}'
        
        # Add the adverb
        if self.adverb:
            adverb = self.adverb.to_text()
            result = f'{result} {adverb}'
        
        # Add prepositional phrases
        if self.pps:
            for pp in self.pps:
                result = f'{result} {pp.to_text()}'

        return result



    def __eq__(self, other: FrameEvent) -> bool:
        if self.subj == other.subj and self.dobj == other.dobj and self.verb == other.verb:
            s1 = sorted(self.pps, key=lambda x: x.key)
            s2 = sorted(other.pps, key=lambda x: x.key)
            if len(s1) == len(s2):
                for i in range(len(s1)):
                    if s1[i] != s2[i]:
                        return False
                
                return True
        return False

    def is_complete(self):
        # Make this more complex
        return self.subj and self.verb
    

    def get_event_name(self): #Pascal case
        result = f'{self.verb.lemma.title()}' # PascalCase: VerbAdverb ?

        adverb = self.adverb
        if adverb:
            result += f'{adverb.adverb_str.title()}'\
        
        return result
