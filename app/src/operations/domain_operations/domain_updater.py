from app.classes.symboleo_contract import SymboleoContract
from app.src.operations.contract_updater import IUpdateContractOp

from app.classes.spec.domain_model import DomainObject
from app.classes.spec.declaration import Declaration

from app.src.operations.domain_operations.dm_object_adder import IAddDomainObjects
from app.src.operations.domain_operations.declaration_adder import IAddDeclarations


class DomainOperation:
    def __init__(
        self,
        obj_type: str,
        domain_obj: DomainObject,
        declaration: Declaration
        ):
        self.obj_type = obj_type #assets, roles, events
        self.domain_obj = domain_obj
        self.declaration = declaration
        

class DomainUpdater(IUpdateContractOp):
    def __init__(
        self,
        domain_object_adder: IAddDomainObjects,
        declaration_adder: IAddDeclarations
    ):
        self.__domain_object_adder = domain_object_adder
        self.__declaration_adder = declaration_adder

    def update(self, contract: SymboleoContract, operation: DomainOperation) -> SymboleoContract:
        contract = self.__domain_object_adder.add(operation.obj_type, contract, operation.domain_obj)
        contract = self.__declaration_adder.add(contract, operation.declaration)
        return contract