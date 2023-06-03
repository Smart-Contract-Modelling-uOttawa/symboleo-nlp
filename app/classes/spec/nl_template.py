from __future__ import annotations
from typing import Dict, List
from app.classes.spec.parameter_config import ParameterConfig
from app.classes.helpers.list_eq import ClassHelpers


class TemplateObj:
    def __init__(self, str_val:str, parameters: Dict[str, List[ParameterConfig]] = None):
        self.str_val = str_val
        self.parameters = parameters
    
    def __eq__(self, other: TemplateObj) -> bool:
        return self.str_val == other.str_val
    
class NLTemplate:
    def __init__(
        self,
        template_dict: Dict[str, TemplateObj]
    ):
        self.template_dict = template_dict
    
    def __eq__(self, other: NLTemplate) -> bool:
        return ClassHelpers.dicts_eq(self.template_dict, other.template_dict)

    def stringify(self):
        result = ''
        for x in self.template_dict:
            str_val = self.template_dict[x].str_val
            result += f'{x}: {str_val}\n'
        
        return result
