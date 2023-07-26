from enum import Enum
from typing import List

class PatternClassType(Enum):
    CONDITIONAL = 'CONDITIONAL'
    TEMPORAL = 'TEMPORAL'
    EXCEPTION = 'EXCEPTION'

class ParameterConfig:
    def __init__(self, norm_type: str, norm_id: str, norm_component: str = '', pattern_types = None):
        self.norm_type = norm_type # obligations, powers 
        self.norm_id = norm_id # e.g. ob_delivery
        self.norm_component = norm_component # consequent, antecedent, trigger
        self.filled = False
        self.pattern_types: List[PatternClassType] = pattern_types or []

