from typing import Dict
from app.src.operations.refine_parameter.parm_configs import ParameterConfig
from app.src.operations.refine_parameter.parameter_refiner import ParameterOperation
from app.src.user_scripts.main_ops.user_deps import UserDependencies
from app.classes.spec.symboleo_contract import SymboleoContract, Norm
from app.src.grammar.grammar_config import GrammarGeneratorConfig

def refine_parm(deps: UserDependencies, contract: SymboleoContract):
    # Choose the string key to refine
    nd = contract.nl_template.template_dict
    kl = list(nd.keys())

    for i,k in enumerate(kl):
        print(f'{i+1}: {k}')

    sel_k = int(input('\nSelect the text # to refine: '))
    key = kl[sel_k-1]
    parm = nd[key]

    # Get the norm and op_codes
    norm: Norm = contract.contract_spec.obligations[parm.mapping[0].split('.')[1]]
    op_codes = norm.get_op_codes()

    grammar_config = GrammarGeneratorConfig(op_codes)
    grammar_root = deps.gg.generate(contract, grammar_config)
    selection = deps.gs.select(grammar_root)

    parm_config = ParameterConfig(
        'obligations',
        norm.id
    )
    parm_op = ParameterOperation(parm_config, selection, key)
    deps.parm_refiner.refine(contract, parm_op)
