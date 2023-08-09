from __future__ import annotations
from enum import Enum
from typing import List

from app.classes.helpers.list_eq import ClassHelpers

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

    def to_string(self):
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
            verb_types: List[VerbType],
            conjugations: VerbConjugations
        ):
        self.verb_str = verb_str
        self.lemma = lemma
        self.verb_types = verb_types # This is a list because sometimes we cannot be certain
        self.conjugations = conjugations
    
    def print_me(self):
        print(f'Verb String: {self.verb_str}')
        print(f'Lemma: {self.lemma}')
        print(f'Verb Types: {", ".join([x.name for x in self.verb_types])}')
        conj_str = self.conjugations.to_string()
        print(f'Conjugations:\n{conj_str}')


    def __eq__(self, other: Verb) -> bool:
        vt1 = [x.name for x in self.verb_types]
        vt2 = [x.name for x in other.verb_types]
        return self.verb_str == other.verb_str and \
            self.lemma == other.lemma and \
            self.conjugations == other.conjugations and \
            ClassHelpers.simple_lists_eq(vt1, vt2)



# NOTE: Used ChatGPT to generate these lists
class VerbLists:
    intransitive_verbs = [ 'abide', 'accrue', 'acquiesce', 'agree', 'appear', 'arise', 'assert', 'assume', 'attend',    'belong', 'cease', 'commence', 'comply', 'concur', 'confess', 'consent', 'continue',    'decline', 'defend', 'delay', 'depart', 'desist', 'devolve', 'disappear', 'discontinue',    'emerge', 'end', 'enforce', 'entitle', 'erupt', 'evolve', 'exist', 'expire', 'fall',    'fluctuate', 'follow', 'function', 'happen', 'incur', 'indemnify', 'inform', 'insist', 'interfere', 'intervene', 'involve', 'issue', 'last', 'lie', 'linger', 'live', 'materialize',    'mature', 'occur', 'operate', 'pass', 'persist', 'prevail', 'proceed', 'recur', 'refrain',    'remain', 'renew', 'reside', 'result', 'revolve', 'return', 'rise', 'run', 'satisfy', 'start', 'stop',    'subsist', 'succeed', 'supervene', 'survive', 'suspend', 'terminate', 'transpire', 'turn',    'vary', 'vest', 'violate', 'waive', 'wane', 'wind', 'worsen']

    transitive_verbs = [ "submit", "accept", "acknowledge", "agree", "allocate", "amend", "annex", "assign", "authorize", "award", "cancel", "certify", "change", "cite", "claim", "compensate", "comply", "confirm", "consent",     "consider", "constitute", "construct", "contemplate", "continue", "contract", "convey", "cooperate",     "correct", "create", "cure", "declare", "deliver", "demonstrate", "designate", "determine", "deviate",     "discharge", "disclose", "discount", "dismiss", "distribute", "document", "draft", "eliminate",     "embody", "employ", "enforce", "establish", "evaluate", "execute", "exercise", "exhibit", "expand",     "expire", "explain", "express", "extend", "facilitate", "finalize", "fulfill", "grant", "guarantee",     "identify", "impose", "incur", "indemnify", "inform", "inquire", "insure", "interpret", "investigate",     "issue", "keep", "maintain", "make", "modify", "negotiate", "notify", "obtain", "offer", "operate",     "order", "pay", "perform", "permit", "possess", "prepare", "prevent", "process", "prohibit",     "promote", "propose", "protect", "provide", "publish", "purchase", "ratify", "receive", "recognize",     "recover", "reduce", "register", "reimburse", "renew", "report", "represent", "request", "reserve",     "restrict", 'return', "revoke", "seek", "select", "settle", "specify", "state", "substantiate", "succeed",     "surrender", "terminate", "transfer", "undertake", "unilaterally", "validate", "vary", "waive"]

    linking_verbs = ['be', 'is', 'am', 'are', 'was', 'were', 'been', 'being', 'seem', 'appear', 'become', 'feel', 'grow', 'look', 'remain', 'smell', 'sound', 'stay', 'taste', 'turn', 'prove', 'get', 'get to be', 'come', 'continue']