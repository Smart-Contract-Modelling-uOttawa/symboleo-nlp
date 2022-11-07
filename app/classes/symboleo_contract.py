class DomainModel:
    s = 0

class ContractSpec:
    s = 0

class SymboleoContract:
    domain_model: DomainModel
    contract_spec: ContractSpec

    def __init__(self, domain_model: DomainModel, contract_spec: ContractSpec):
        self.domain_model = domain_model
        self.contract_spec = contract_spec

