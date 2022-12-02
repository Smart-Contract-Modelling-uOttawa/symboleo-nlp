from typing import List
from app.classes.spec.primitive import Primitive
from app.src.primitive_identifiers.primitive_identifier import IIdentifyPrimitives

# TODO: Add in all the types here
class PredicateExtractorConfig:
    def __init__(
        self,
        template,
        matcher,
        case_dict,
        target_primitives: List[Primitive],
        default_components
    ):
        self.template = template
        self.matcher = matcher
        self.case_dict = case_dict
        self.target_primitives = target_primitives
        self.default_components = default_components


class DomainPropProcessorConfig:
    def __init__(
        self, 
        obj_type: str,
        obj_name: str,
        new_prop_name: str,
        new_prop_type: str ='str'
    ):
        self.obj_type = obj_type
        self.obj_name = obj_name
        self.new_prop_name = new_prop_name
        self.new_prop_type = new_prop_type


class PredicateProcessorConfig:
    def __init__(self, norm_type, norm_id, norm_component):
        self.norm_type = norm_type # obligations, powers 
        self.norm_id = norm_id # e.g. delivery
        self.norm_component = norm_component # consequent, antecedent, ...