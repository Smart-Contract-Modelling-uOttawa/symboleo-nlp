from typing import Dict
from app.src.operations.parm_configs import ParameterSpec, ParameterConfig
from app.src.operations.parameter_refiner import ParameterOperation
from app.src.user_scripts.main_ops.user_deps import UserDependencies
from app.classes.symboleo_contract import SymboleoContract, Norm
from app.src.grammar.grammar_config import GrammarGeneratorConfig

def refine_parm(deps: UserDependencies, contract: SymboleoContract):
    # Choose the string key to refine
    nd = contract.nl_template.template_dict
    kl = list(nd.keys())

    for i,k in enumerate(kl):
        print(f'{i+1}: {k}')

    sel_k = int(input('\nSelect the text # to refine: '))
    parm = nd[kl[sel_k-1]]

    # Get the norm and op_codes
    norm: Norm = contract.contract_spec.obligations[parm.mapping[0].split('.')[1]]
    op_codes = norm.get_op_codes()

    grammar_config = GrammarGeneratorConfig(op_codes)
    grammar_root = deps.gg.generate(contract, grammar_config)
    selection = deps.gs.select(grammar_root)

    parm_config = ParameterConfig(
        'obligations',
        norm.id,
        '' 
    )
    # Want to get rid of the ParmOperation/ParmConfig; just pass the norm in (or norm id)
    ## e.g. refine(contract, norm, selection)
    parm_op = ParameterOperation(parm_config, selection)
    deps.parm_refiner.refine(contract, parm_op)



# TODO: Goal is to get rid of parameters. Choose an obligation to refine instead
def refine_parm_old(deps: UserDependencies, contract: SymboleoContract, parameters: Dict[str, ParameterSpec]):
    # Gather the required input
    pki_dict = {i+1: pk for i,pk in enumerate(parameters)}

    for pki in pki_dict:
        print(f'{pki} - {pki_dict[pki]}')

    selected_pki = input('Select a parameter: ')
    selected_pk = pki_dict[int(selected_pki)]
    parm_spec = parameters[selected_pk]

    print(f'\nParameter: {selected_pk}')

    # Collect the parameter info
    grammar_config = GrammarGeneratorConfig(parm_spec.op_codes)
    grammar_root = deps.gg.generate(contract, grammar_config)
    selection = deps.gs.select(grammar_root)

    # Refine
    parm_op = ParameterOperation(parm_spec.configs[0], selection)
    deps.parm_refiner.refine(contract, parm_op)
