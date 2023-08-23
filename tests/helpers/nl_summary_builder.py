from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.nl_template import NLTemplate

class NLSummaryBuilder:
    @staticmethod
    def build(c1: SymboleoContract, c2: SymboleoContract) -> str:
        nl_summary = ''
        for xk in c1.nl_template.template_dict:
            act_x = c1.nl_template.template_dict[xk].str_val
            
            if xk in c2.nl_template.template_dict:
                exp_x = c2.nl_template.template_dict[xk].str_val
            else:
                exp_x = ''
            nl_summary += f'A - {xk}: {act_x}\nE - {xk}: {exp_x}\n\n'
        
        for xk in c2.nl_template.template_dict:
            act_x = ''
            if xk not in c1.nl_template.template_dict:
                exp_x = c2.nl_template.template_dict[xk].str_val
                nl_summary += f'A - {xk}: {act_x}\nE - {xk}: {exp_x}\n\n'
            
        return nl_summary