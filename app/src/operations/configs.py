from enum import Enum

# class syntax
class OpCode(Enum):
    ADD_DM_PROP = 1
    REFINE_PREDICATE = 2
    ADD_TRIGGER = 3
    ADD_NORM = 4 

# Since it may be possible for a parm to have EITHER result (domain prop OR predicate processing),
# We should only have one single config object type. Just lump them together
# Just use the PredicateProcessorConfig, but change the name - ParameterConfig 
class DomainPropProcessorConfig:
    def __init__(
        self, 
        obj_type: str,
        obj_name: str
    ):
        self.obj_type = obj_type # role, asset, event
        self.obj_name = obj_name


class PredicateProcessorConfig:
    def __init__(self, norm_type, norm_id, norm_component, dm_obj_type='', dm_obj_name=''):
        self.norm_type = norm_type # obligations, powers 
        self.norm_id = norm_id # e.g. delivery
        self.norm_component = norm_component # consequent, antecedent, ...

        self.obj_type = dm_obj_type # role, asset, event
        self.obj_name = dm_obj_name # e.g. evt_payment

