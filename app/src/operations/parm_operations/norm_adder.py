import copy
from app.classes.symboleo_contract import SymboleoContract
from app.classes.spec.contract_spec import Norm, Obligation, Power

class IAddNorms:
    def add(self, contract: SymboleoContract, new_norm: Norm) -> SymboleoContract:
        raise NotImplementedError() 


class NormAdder(IAddNorms):
    def add(self, contract: SymboleoContract, new_norm: Norm) -> SymboleoContract:
        # Get the norm type
        norm_type = 'obligations' if type(new_norm) == Obligation else 'powers'
        # Add the norm
        new_spec = copy.deepcopy(contract.contract_spec)
        new_spec.__dict__[norm_type][new_norm.id] = new_norm

        # Return the updated Symboleo Contract
        return SymboleoContract(contract.domain_model, new_spec, contract.nl_template)
