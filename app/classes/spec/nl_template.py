from typing import Dict, List

class TemplateObj:
    def __init__(self, str_val:str, mapping: List[str]):
        self.str_val = str_val
        self.mapping = mapping
    
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
