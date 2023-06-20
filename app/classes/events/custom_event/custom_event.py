from __future__ import annotations
from typing import List
from app.classes.spec.sym_event import VariableEvent, ContractEvent, ContractEventName, ObligationEvent, ObligationEventName
from app.classes.events.conj_type import ConjType

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
        event_key:str = '',
        is_new: bool = True
    ):
        self.subj = subj
        self.verb = verb
        self.adverb = adverb
        self.dobj = dobj
        self.predicate = predicate
        self.pps = pps
        self.negation = negation
        self.event_type = ''
        self.is_new = is_new

    def event_key(self):
        # This will change. Might be a function of the event itself...
        if VerbType.TRANSITIVE in self.verb.verb_types:
            event_key = f'evt_{self.verb.lemma}_{self.dobj.head}'
        else:
            event_key = f'evt_{self.verb.lemma}'
        return event_key
            

    # kill?
    def to_sym_event(self):
        if self.event_type == 'contract':
            return ContractEvent(ContractEventName[self.verb.verb_str.capitalize()])
        else:
            name = self.get_declaration_name()
            snake_name = CaseConverter.to_snake(name)
            return VariableEvent(f'evt_{snake_name}')

    def get_declaration_name(self):
        name = self.verb.lemma.lower()

        if VerbType.LINKING in self.verb.verb_types and len(self.verb.verb_types) == 1:
            name = CaseConverter.to_pascal(f'{self.subj.to_text()} {self.predicate.pred_str}')
        
        if VerbType.TRANSITIVE in self.verb.verb_types:
            name = self.verb.lemma.title()

            if self.adverb:
                name = f'{name}{self.adverb.adverb_str.title()}'
        
        return name 

    # TODO: E2? - Add tests for custom_event.to_text
    ## It's possible we wont even need this - depends on how we generate the NL refinement
    ## Most of it may get pushed to the input phase, rather than handling it here
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

    # TODO: E1? - This may not be needed either
    def is_complete(self):
        return True
        #return self.subj and self.verb

