from __future__ import annotations
from typing import List
from app.classes.events.conj_type import ConjType
from app.classes.events.custom_event.noun_phrase import NPTextType

from app.classes.events.base_event import BaseEvent

from app.classes.events.custom_event.noun_phrase import NounPhrase
from app.classes.events.custom_event.verb import Verb, VerbType
from app.classes.events.custom_event.predicate import Predicate
from app.classes.events.custom_event.adverb import Adverb
from app.classes.events.custom_event.prep_phrase import PrepPhrase

from app.classes.helpers.list_eq import ClassHelpers
from app.classes.helpers.string_to_class import CaseConverter

class CustomEvent(BaseEvent):
    def __init__(
        self, 
        subj: NounPhrase = None, 
        verb: Verb = None, 
        adverb: Adverb = None, 
        dobj: NounPhrase = None, 
        predicate: Predicate = None, 
        pps:List[PrepPhrase] = None,
        negation:bool = False,
        is_new: bool = True
    ):
        self.subj = subj
        self.verb = verb
        self.adverb = adverb
        self.dobj = dobj
        self.predicate = predicate
        self.pps = pps
        self.negation = negation
        self.is_new = is_new


    def event_key(self):
        a = self._split_name()
        b = a.split(' ')
        c = [x.lower() for x in b]
        d = '_'.join(c)
        e = f'evt_{d}'
        return e

    def get_declaration_name(self):
        a = self._split_name()
        b = a.split(' ')
        c = [x.title() for x in b]
        return ''.join(c)
    

    # Return space-sep
    def _split_name(self):
        result = self.verb.lemma

        if VerbType.LINKING in self.verb.verb_types and len(self.verb.verb_types) == 1:
            result = f'{self.subj.to_text(NPTextType.BASIC)} {self.predicate.pred_str}'
        
        if VerbType.TRANSITIVE in self.verb.verb_types:

            if self.adverb:
                result = f'{result} {self.adverb.adverb_str}'

        return result

    def to_text(self, conjugation: ConjType = ConjType.PRESENT):
        
        subj = self.subj.to_text()
        result = subj

        if self.negation:
            if self.subj.is_plural:
                result += ' fail to'
            else:
                result += ' fails to'

        if conjugation == ConjType.PRESENT:
            if self.subj.is_plural:
                verb = self.verb.conjugations.present_singular
            else:
                if self.negation:
                    verb = self.verb.conjugations.present_singular
                else:
                    verb = self.verb.conjugations.present_plural

        elif conjugation == ConjType.CONTINUOUS:
            verb = self.verb.conjugations.continuous
        
        elif conjugation == ConjType.BASIC:
            verb = self.verb.verb_str
    

        if self.dobj and VerbType.TRANSITIVE in self.verb.verb_types:
            dobj = self.dobj.to_text()
            result += f' {verb} {dobj}'

        elif VerbType.INTRANSITIVE in self.verb.verb_types:
            result += f' {verb}'
        
        elif VerbType.LINKING in self.verb.verb_types:
            if self.predicate:
                pred = self.predicate.to_text()
                result += f' {verb} {pred}'
            
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


