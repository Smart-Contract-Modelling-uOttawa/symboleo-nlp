import copy
from app.src.operations.parm_operations.parameter_updater import IUpdateParameter
from app.src.operations.parm_operations.configs import ParameterConfig
from app.classes.symboleo_contract import SymboleoContract
from app.classes.spec.contract_spec import Norm, Obligation


class NormAdder(IUpdateParameter):
    def update(self, contract: SymboleoContract, config: ParameterConfig, update_obj: Norm):
        # Get the norm type
        new_norm = update_obj
        norm_type = 'obligations' if type(new_norm) == Obligation else 'powers'
        # Add the norm
        new_spec = copy.deepcopy(contract.contract_spec)
        new_spec.__dict__[norm_type][new_norm.id] = new_norm

        # Return the updated Symboleo Contract
        return SymboleoContract(contract.domain_model, new_spec, contract.nl_template)
