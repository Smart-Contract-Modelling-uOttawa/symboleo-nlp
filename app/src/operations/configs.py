from typing import List
from enum import Enum

# class syntax
class OpCode(Enum):
    ADD_DM_PROP = 1
    REFINE_PREDICATE = 2
    ADD_TRIGGER = 3
    ADD_NORM = 4 


class ParameterConfig:
    def __init__(self, norm_type, norm_id, norm_component, dm_obj_type='', dm_obj_name='', op_codes: List[OpCode] = [] ):
        self.norm_type = norm_type # obligations, powers 
        self.norm_id = norm_id # e.g. delivery
        self.norm_component = norm_component # consequent, antecedent, ...

        self.obj_type = dm_obj_type # role, asset, event
        self.obj_name = dm_obj_name # e.g. evt_payment
        self.op_codes = op_codes


