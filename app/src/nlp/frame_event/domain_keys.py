from enum import Enum

# How do I populate this
## This cannot be exhaustive...
## Would like to populate it using FrameNet elements
## But then the precise mapping is difficult. Need to connect them
## Map FrameNet to Declaration. This is trivial
## Hard: Map CustomEvent to FrameNet  
class DomainKeys(Enum):
    AGENT = 'agent'
    TARGET = 'target'
    AMOUNT = 'amount'
    METHOD = 'method'
    OTHER = 'other'
    #...


