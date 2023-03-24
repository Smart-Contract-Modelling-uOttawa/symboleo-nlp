import copy
from app.src.operations.parm_operations.parameter_updater import IUpdateParameter
from app.classes.symboleo_contract import SymboleoContract
from app.classes.spec.domain_model import DomainProp
from app.src.operations.parm_operations.configs import ParameterConfig

# Processes and updates a domain prop
# Could be built to handle updates to existing DM props AND adding new ones...
class DomainPropAdder(IUpdateParameter):
    def update(self, contract: SymboleoContract, config: ParameterConfig, update_obj: DomainProp):
        new_dm = copy.deepcopy(contract.domain_model)
        new_dm.__dict__[config.obj_type][config.obj_name].props.append(update_obj)

        return SymboleoContract(new_dm, contract.contract_spec, contract.nl_template)
