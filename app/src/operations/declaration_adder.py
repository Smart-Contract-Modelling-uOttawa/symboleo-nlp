import copy
from app.classes.symboleo_contract import SymboleoContract
from app.classes.spec.declaration import Declaration

class IAddDeclarations:
    def add(self, contract: SymboleoContract, declaration: Declaration) -> SymboleoContract:
        raise NotImplementedError()

class DeclarationAdder(IAddDeclarations):
    def add(self, contract: SymboleoContract, declaration: Declaration) -> SymboleoContract:
        new_cs = copy.deepcopy(contract.contract_spec)
        new_cs.declarations[declaration.name] = declaration
        return SymboleoContract(contract.domain_model, new_cs, contract.nl_template)
