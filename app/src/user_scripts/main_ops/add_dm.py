from app.src.user_scripts.main_ops.user_deps import UserDependencies
from app.classes.symboleo_contract import SymboleoContract

from app.src.user_scripts.domain_event_creator import DomainEventCreator
from app.src.user_scripts.declarer import ManualDeclarer

from app.src.operations.domain_updater import DomainOperation

def add_dm(deps: UserDependencies, contract: SymboleoContract):
    print('\nAdding a new domain event...\n')
    dmc = DomainEventCreator(contract.domain_model)
    domain_event = dmc.create()

    print('\nInstantiating the event...\n')
    declaration = ManualDeclarer.declare_input(contract, domain_event, 'events')

    op = DomainOperation(domain_event, declaration)
    deps.domain_updater.update(contract, op)



