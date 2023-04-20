from enum import Enum

class NodeType(Enum):
    ROOT = 1,
    EVENT = 10,
    DATE = 11,
    BEFORE = 12,
    TIMESPAN = 13,
    WITHIN = 14,
    IF = 15,
    DUMMY = 17,
    AFTER = 18,
    UNTIL = 19,
    TIMEPOINT = 22,
    DOMAIN_TIMEPOINT = 23,
    SUBJECT = 24,
    VERB = 25,
    NEW_EVENT = 26,
    STANDARD_EVENT = 27,
    CONTRACT_SUBJECT = 28,
    CONTRACT_ACTION = 29,
    PREDICATE = 30,
    ADVERB = 31,
    DOBJ = 32,
    PREP_PHRASE = 33
    # ....