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
from app.classes.helpers.case_converter import CaseConverter

class CustomEvent(BaseEvent):
    def __init__(
        self, 
        subj: NounPhrase = None, 
        verb: Verb = None, 
        adverb: Adverb = None, 
        dobj: NounPhrase = None, 
        predicate: Predicate = None, 
        pps:List[PrepPhrase] = None,
        is_new: bool = True
    ):
        self.subj = subj
        self.verb = verb
        self.adverb = adverb
        self.dobj = dobj
        self.predicate = predicate
        self.pps = pps
        self.is_new = is_new


    def event_key(self):
        a = self._split_name()
        c = [x.lower() for x in a.split(' ')]
        d = '_'.join(c)
        e = f'evt_{d}'
        return e

    def get_declaration_name(self):
        a = self._split_name()
        c = [x.title() for x in a.split(' ')]
        return ''.join(c)
    

    def _split_name(self) -> str:
        # ROLE, VERB, OBJ
        a = []

        # ROLE
        if self.verb.verb_type in [VerbType.LINKING, VerbType.INTRANSITIVE]:
            if self.subj.is_role:
                a.append('agent')
            else:
                a.append(self.subj.to_text(NPTextType.BASIC))

        # VERB
        if self.verb.verb_type in [VerbType.TRANSITIVE, VerbType.INTRANSITIVE]:
            a.append(self.verb.lemma)
        
        # OBJ
        if self.verb.verb_type == VerbType.TRANSITIVE:
            if self.dobj.is_parm:
                split_parm = self.dobj.str_val[1:-1].replace('_', ' ').lower()
                a.append(split_parm)
            elif self.dobj.asset_type != 'Money':
                    a.append(self.dobj.head)

        elif self.verb.verb_type == VerbType.LINKING:
            a.append(self.predicate.pred_str)
        
        if self.adverb:
            a.append(self.adverb.adverb_str)
        
        return ' '.join(a)


    def __eq__(self, other: CustomEvent) -> bool:
        return self.subj == other.subj and \
            self.dobj == other.dobj and \
            self.verb == other.verb and \
            self.adverb == other.adverb and \
            self.predicate == other.predicate and \
            ClassHelpers.lists_eq(self.pps, other.pps, 'pp_str')


