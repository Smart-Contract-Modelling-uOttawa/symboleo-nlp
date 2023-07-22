from typing import Tuple
from app.classes.spec.symboleo_contract import SymboleoContract

class IGetParm:
    def get(self, contract: SymboleoContract) -> Tuple[str,str]:
        raise NotImplementedError()

class ParmGetter(IGetParm):
    def get(self, contract: SymboleoContract) -> Tuple[str, str]:
        nd = contract.nl_template.template_dict
        
        # Select NL Key
        kl = list(nd.keys())

        for i,k in enumerate(kl):
            print(f'{i+1}: {k}')

        sel_nl_key = int(input('\nSelect the text # to refine: '))
        
        nl_key = kl[sel_nl_key-1]

        # Select Parm Key
        parm_keys = list(nd[nl_key].parameters.keys())
        for i,k in enumerate(list(parm_keys)):
            print(f'{i+1}: {k}')
        
        sel_parm_key = int(input('\nSelect the parameter # to refine: '))
        
        parm_key = parm_keys[sel_parm_key-1]

        return nl_key, parm_key