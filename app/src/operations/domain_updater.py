from app.classes.spec.symboleo_contract import SymboleoContract

from app.classes.spec.domain_object import DomainObject
from app.classes.spec.declaration import Declaration

class DomainOperation:
    def __init__(
        self,
        domain_obj: DomainObject,
        declaration: Declaration
        ):
        self.domain_obj = domain_obj
        self.declaration = declaration
        
class IUpdateDomain:
    def update(self, contract: SymboleoContract, operation: DomainOperation) -> SymboleoContract:
        raise NotImplementedError()

class DomainUpdater(IUpdateDomain):
    def update(self, contract: SymboleoContract, operation: DomainOperation) -> SymboleoContract:
        contract.add_dm_object(operation.domain_obj)
        contract.add_declaration(operation.declaration)
