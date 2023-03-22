import copy
from app.classes.symboleo_contract import SymboleoContract
from app.classes.spec.domain_model import DomainObject
from app.src.operations.configs import ParameterConfig

class IAddDomainObjects:
    def add(self, obj_type: str, contract: SymboleoContract, new_obj: DomainObject) -> SymboleoContract:
        raise NotImplementedError()

class DomainObjectAdder(IAddDomainObjects):
    def add(self, obj_type: str, contract: SymboleoContract, new_obj: DomainObject) -> SymboleoContract:
        new_dm = copy.deepcopy(contract.domain_model)
        new_dm.__dict__[obj_type][new_obj.name] = new_obj
        return SymboleoContract(new_dm, contract.contract_spec, contract.nl_template)
