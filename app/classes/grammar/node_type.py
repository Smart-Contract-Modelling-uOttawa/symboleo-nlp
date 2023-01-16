from enum import Enum

class NodeType(Enum):
    ROOT = 1,
    CONTRACT_EVENT_ACTION = 3,
    CONTRACT_EVENT = 4,
    DOMAIN_EVENT_NAME = 5,
    DOMAIN_EVENT = 6,
    OBLIGATION_EVENT_ACTION = 7,
    OBLIGATION_EVENT_VAR = 8,
    OBLIGATION_EVENT = 9,
    EVENT = 10,
    DATE = 11,
    BEFORE = 12,
    TIMESPAN = 13,
    WITHIN = 14
    # ....