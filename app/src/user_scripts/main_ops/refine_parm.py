from typing import Dict
from app.src.operations.parm_configs import ParameterSpec
from app.src.operations.parameter_refiner import ParameterOperation
from app.src.user_scripts.main_ops.user_deps import UserDependencies
from app.classes.symboleo_contract import SymboleoContract
from app.src.grammar.grammar_config import GrammarGeneratorConfig

def refine_parm(deps: UserDependencies, contract: SymboleoContract, parameters: Dict[str, ParameterSpec]):
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
