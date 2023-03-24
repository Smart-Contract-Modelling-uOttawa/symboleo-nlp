import copy
from app.classes.symboleo_contract import SymboleoContract
from app.classes.spec.domain_model import DomainProp
from app.src.operations.parm_operations.configs import ParameterConfig

class IAddDomainProps:
    def add(self, config: ParameterConfig, contract: SymboleoContract, new_prop: DomainProp) -> SymboleoContract:
        raise NotImplementedError()


# Processes and updates a domain prop
# Could be built to handle updates to existing DM props AND adding new ones...
class DomainPropAdder(IAddDomainProps):

    def add(self, config: ParameterConfig, contract: SymboleoContract, new_prop: DomainProp) -> SymboleoContract:
        new_dm = copy.deepcopy(contract.domain_model)
        new_dm.__dict__[config.obj_type][config.obj_name].props.append(new_prop)

        return SymboleoContract(new_dm, contract.contract_spec, contract.nl_template)
