from typing import List
from enum import Enum

# Might not actually need these...
class ParmOpCode(Enum):
    ADD_DM_PROP = 1 # TODO: May actually remove this one...
    REFINE_PREDICATE = 2
    ADD_TRIGGER = 3
    ADD_NORM = 4 

# Might not need this either...
class ParameterConfig:
    def __init__(self, norm_type: str, norm_id: str, norm_component: str = ''):
        self.norm_type = norm_type # obligations, powers 
        self.norm_id = norm_id # e.g. ob_delivery
        self.norm_component = norm_component # consequent, antecedent, trigger
