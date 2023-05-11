from typing import List
from enum import Enum

# Might not actually need these...
# Will likely change this one a bit. Ignore it for now, but will need to bring it back
class ParmOpCode(Enum):
    ADD_DM_PROP = 1 # TODO: May actually remove this one...
    REFINE_PREDICATE = 2
    ADD_TRIGGER = 3
    ADD_NORM = 4 

