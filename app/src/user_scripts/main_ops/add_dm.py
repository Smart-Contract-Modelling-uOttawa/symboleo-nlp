from app.src.user_scripts.main_ops.user_deps import UserDependencies
from app.classes.symboleo_contract import SymboleoContract

from app.src.user_scripts.domain_event_creator import DomainEventCreator
from app.src.user_scripts.declarer import ManualDeclarer
from app.src.operations.domain_operations.dm_object_adder import DomainObjectAdder
from app.src.operations.domain_operations.declaration_adder import DeclarationAdder


def add_dm(deps: UserDependencies, contract: SymboleoContract):
    print('\nAdding a new domain event...\n')
    dmc = DomainEventCreator(contract.domain_model)
    domain_event = dmc.create()

    dm_adder = DomainObjectAdder()
    contract = dm_adder.add('events', contract, domain_event)

    print('\nInstantiating the event...\n')
    declaration = ManualDeclarer.declare_input(contract, domain_event, 'events')

    # Will need to add to the declaration - separate operation
    declaration_adder = DeclarationAdder()
    contract = declaration_adder.add(contract, declaration)

    return contract


