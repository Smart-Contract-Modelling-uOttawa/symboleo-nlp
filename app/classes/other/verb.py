from __future__ import annotations
from enum import Enum
from typing import List

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


class Verb:
    # May add negation flag
    def __init__(
            self, 
            verb_str: str,
            lemma: str, 
            verb_types: List[VerbType],
            conjugations: VerbConjugations
        ):
        self.verb_str = verb_str # original
        self.lemma = lemma
        self.verb_types = verb_types # This is a list because sometimes we cannot be sure
        self.conjugations = conjugations
    
    def __eq__(self, other: Verb) -> bool:
        return self.lemma == other.lemma


    def print_me(self):
        print(f'- Lemma: {self.lemma}')