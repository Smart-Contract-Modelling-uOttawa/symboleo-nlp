from __future__ import annotations
from enum import Enum

class VerbType(Enum):
    LINKING = 'linking',
    TRANSITIVE = 'transitive',
    INTRANSITIVE = 'intransitive'

class VerbConjugations:
    def __init__(self, present_singular, present_plural, past, continuous):
        self.present_singular = present_singular
        self.present_plural = present_plural
        self.past = past
        self.continuous = continuous

    def to_string(self): # pragma: no cover
        return f'- present singular: {self.present_singular}\n' + \
            f'- present plural: {self.present_plural}\n' + \
            f'- preterite: {self.past}\n' + \
            f'- continuous: {self.continuous}\n'
    
    def __eq__(self, __value: VerbConjugations) -> bool:
        return self.present_plural == __value.present_plural and \
            self.present_singular == __value.present_singular and \
            self.continuous == __value.continuous and \
            self.past == __value.past

class Verb:
    def __init__(
            self, 
            verb_str: str,
            lemma: str, 
            verb_type: VerbType,
            conjugations: VerbConjugations
        ):
        self.verb_str = verb_str
        self.lemma = lemma
        self.verb_type = verb_type
        self.conjugations = conjugations
    
    def print_me(self): # pragma: no cover
        print(f'Verb String: {self.verb_str}')
        print(f'Lemma: {self.lemma}')
        print(f'Verb Type: {self.verb_type.value}')
        conj_str = self.conjugations.to_string()
        print(f'Conjugations:\n{conj_str}')


    def __eq__(self, other: Verb) -> bool:
        return self.verb_str == other.verb_str and \
            self.lemma == other.lemma and \
            self.conjugations == other.conjugations and \
            self.verb_type == other.verb_type
