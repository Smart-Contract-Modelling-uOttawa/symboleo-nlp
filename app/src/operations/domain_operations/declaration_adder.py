import copy
from app.classes.symboleo_contract import SymboleoContract
from app.classes.spec.declaration import Declaration
from app.classes.spec.contract_spec_other import ContractSpecParameter

class IAddDeclarations:
    def add(self, contract: SymboleoContract, declaration: Declaration) -> SymboleoContract:
        raise NotImplementedError()

class DeclarationAdder(IAddDeclarations):
    def add(self, contract: SymboleoContract, declaration: Declaration) -> SymboleoContract:
        # Add the declaration
        new_cs = copy.deepcopy(contract.contract_spec)
        new_cs.declarations[declaration.name] = declaration

        # Add any new parameters as well
        parm_names = [x.name for x in contract.contract_spec.parameters]
        decl_keys = [x for x in contract.contract_spec.declarations]
        for dp in declaration.props:
            if dp.value not in parm_names and dp.value not in decl_keys:
                new_parm = ContractSpecParameter(dp.value, dp.type)
                new_cs.parameters.append(new_parm)

        return SymboleoContract(contract.domain_model, new_cs, contract.nl_template)
