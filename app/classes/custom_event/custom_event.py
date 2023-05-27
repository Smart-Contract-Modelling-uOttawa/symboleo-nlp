from __future__ import annotations
from typing import List
from app.classes.spec.sym_event import VariableEvent, ContractEvent, ContractEventName
from app.classes.custom_event.conj_type import ConjType

from app.classes.custom_event.noun_phrase import NounPhrase
from app.classes.custom_event.verb import Verb, VerbType
from app.classes.custom_event.predicate import Predicate
from app.classes.custom_event.adverb import Adverb
from app.classes.custom_event.prep_phrase import PrepPhrase

from app.classes.other.helpers import ClassHelpers

class CustomEvent:
    def __init__(
        self, 
        subj: NounPhrase = None, 
        verb: Verb = None, 
        adverb: Adverb = None, 
        dobj: NounPhrase = None, 
        predicate: Predicate = None, 
        pps:List[PrepPhrase] = None,
        negation:bool = False
    ):
        self.subj = subj
        self.verb = verb
        self.adverb = adverb
        self.dobj = dobj
        self.predicate = predicate
        self.pps = pps
        self.negation = negation
        self.event_type = ''

    def to_sym_event(self):
        if self.event_type == 'contract':
            return ContractEvent(ContractEventName[self.verb.verb_str.capitalize()])
        else:
            return VariableEvent(self.get_declaration_name())

    # TODO: Will be more complex...
    def get_declaration_name(self):
        p = self.verb.lemma.lower()
        return f'evt_{p}'

    # TODO: This will be more complex. Will need to split it out, potentially into static functions. Need tests
    # Need to incorporate negation
    def to_text(self, conjugation: ConjType = ConjType.PRESENT):
        subj = self.subj.to_text()
        result = subj

        # Some of this may get pushed to the input as well
        ## e.g. maybe we enforce "fails to" vs "fail to" on the input, rather than handling here
        ## Would probably make more sense

        # Will depend on the conjugation type as well...
        # And on plurality...
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

        if self.dobj and VerbType.TRANSITIVE in self.verb.verb_types:
            dobj = self.dobj.to_text()
            result += f' {verb} {dobj}'

        elif VerbType.INTRANSITIVE in self.verb.verb_types:
            result += f' {verb}'
        
        elif VerbType.LINKING in self.verb.verb_types:
            if self.subj.is_plural:
                verb = self.verb.conjugations.present_plural
            else:
                verb = self.verb.conjugations.present_singular
            
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

    # TODO: Make this more complex
    def is_complete(self):
        return True
        #return self.subj and self.verb

