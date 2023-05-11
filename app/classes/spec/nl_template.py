from typing import Dict, List
from app.classes.spec.parameter_config import ParameterConfig

class TemplateObj:
    def __init__(self, str_val:str, parameters: Dict[str, List[ParameterConfig]] = None):
        self.str_val = str_val
        self.parameters = parameters
    
class NLTemplate:
    def __init__(
        self,
        template_dict: Dict[str, TemplateObj]
    ):
        self.template_dict = template_dict
    
    def stringify(self):
        result = ''
        for x in self.template_dict:
            str_val = self.template_dict[x].str_val
            result += f'{x}: {str_val}\n'
        
        return result
