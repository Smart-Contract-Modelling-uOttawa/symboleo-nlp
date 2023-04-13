from app.src.user_scripts.main_ops.user_deps import UserDependencies
from app.classes.spec.symboleo_contract import SymboleoContract
from app.src.grammar.grammar_config import GrammarGeneratorConfig
from app.src.operations.refine_parameter.parm_configs import ParmOpCode
from app.src.operations.add_power.termination_updater import TerminationOperation

# Adding a new termination power
# TODO: Want to change this to just adding ANY power. Since Powers can be fully defined by the domain model
def add_term(deps: UserDependencies, contract: SymboleoContract):
    print('\nAdding termination condition...\n')

    # Collect relevant user input (debtor, id).. May make this another script...
    user_id = input('\nEnter an identifier: ')
    print('\nChoose which role has the power to terminate the contract:\n')

    roles = list(contract.domain_model.roles.keys())
    print(roles)
    for i,x in enumerate(roles):
        print(f'{i+1}: {x}')
    debtor_key = int(input('-- Enter #: ')) - 1

    debtor = roles[debtor_key]
    creditor = roles[1 - debtor_key]
    norm_id = f'termination_{user_id}'

    # Collect parameter info
    grammar_config = GrammarGeneratorConfig([ParmOpCode.ADD_TRIGGER])
    grammar_root = deps.gg.generate(contract, grammar_config)
    selection = deps.gs.select(grammar_root)
    
    op = TerminationOperation(norm_id, debtor, creditor, selection)
    deps.tp_adder.update(contract, op)

