from app.src.operations.domain_operations.domain_updater import DomainUpdater
from app.src.operations.domain_operations.dm_object_adder import DomainObjectAdder
from app.src.operations.domain_operations.declaration_adder import DeclarationAdder

class DomainUpdaterBuilder: # pragma: no cover
    @staticmethod
    def build() -> DomainUpdater:
        do_adder = DomainObjectAdder()
        dec_adder = DeclarationAdder()
        return DomainUpdater(do_adder, dec_adder)