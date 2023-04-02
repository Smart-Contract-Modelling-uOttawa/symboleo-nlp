from app.src.user_scripts.main_ops.user_deps import UserDependencies
from app.classes.symboleo_contract import SymboleoContract
from app.src.grammar.grammar_config import GrammarGeneratorConfig
from app.src.operations.parm_operations.parameter_updater import ParmOpCode
from app.src.operations.parm_operations.configs import ParameterConfig
from app.src.operations.termination_operations.termination_updater_builder import TerminationUpdaterBuilder
from app.src.operations.termination_operations.termination_updater import TerminationOperation

# Adding a new termination power
def add_term(deps: UserDependencies, contract: SymboleoContract) -> SymboleoContract:
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
    
    parm_config = ParameterConfig('powers', norm_id, 'trigger')
    parm_op = deps.poe.extract(contract, parm_config, selection)

    # Perform the update
    tu = TerminationUpdaterBuilder.build()
    term_op = TerminationOperation(norm_id, debtor, creditor, parm_op)
    contract = tu.update(contract, term_op)    
    return contract
