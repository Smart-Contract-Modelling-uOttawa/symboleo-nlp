from app.classes.spec.symboleo_contract import SymboleoContract

from app.src.operations.refine_parameter.parameter_refiner import ParameterOperation
from app.src.user_scripts.main_ops.user_deps import UserDependencies

def refine_parm(deps: UserDependencies, contract: SymboleoContract):
    nd = contract.nl_template.template_dict
    
    # Select NL Keu
    kl = list(nd.keys())

    for i,k in enumerate(kl):
        print(f'{i+1}: {k}')

    sel_k = int(input('\nSelect the text # to refine: '))
    
    key = kl[sel_k-1]

    # Select Parm Key
    parm_keys = nd[key].parameters.keys()
    for i,k in enumerate(list(parm_keys)):
        print(f'{i+1}: {k}')
    
    sel_k = int(input('\nSelect the parameter # to refine: '))
    
    parm_key = kl[sel_k-1]

    # Run selection to build the node list
    selection = deps.gs.select(contract)

    # Run refinement
    deps.parm_refiner.refine(contract, ParameterOperation(key, parm_key, selection))
