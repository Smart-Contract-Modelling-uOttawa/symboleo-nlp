from app.classes.spec.symboleo_contract import SymboleoContract

from app.console_app.console_dependencies import UserDependencies
from app.src.operations.termination_updater import TerminationOperation

# TODO: Re-integrate this?
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
    selection = deps.gs.select(contract)
    
    op = TerminationOperation(norm_id, debtor, creditor, selection)
    deps.tp_adder.update(contract, op)

