from typing import Dict
from app.classes.domain_model.domain_model import Role, DomainEvent, Asset
from app.classes.spec.symboleo_spec import Obligation
from app.classes.spec.symboleo_spec import Power

class DomainModel:
    roles: Dict[str, Role]
    events: Dict[str, DomainEvent]
    assets: Dict[str, Asset]

    def __init__(self, roles, events, assets):
        self.roles = roles
        self.events = events
        self.assets = assets
    
    def to_sym(self):
        result = 'Roles:\n'
        for x in self.roles:
            result += f'{x}: {self.roles[x].to_sym()}\n'
        
        result += '\nAssets:\n'
        for x in self.assets:
            result += f'{x}: {self.assets[x].to_sym()}\n'
        
        result += '\nEvents:\n'
        for x in self.events:
            result += f'{x}: {self.events[x].to_sym()}\n'
        
        return result


class ContractSpec:
    obligations: Dict[str, Obligation]
    powers: Dict[str,Power]

    def __init__(self, obligations, powers):
        self.obligations = obligations
        self.powers = powers
    
    def to_sym(self):
        result = 'Obligations:\n'
        for x in self.obligations:
            result += f'{x}: {self.obligations[x].to_sym()}\n'
        
        result += '\nPowers:\n'
        for x in self.powers:
            result += f'{x}: {self.powers[x].to_sym()}\n'
        
        return result


class SymboleoContract:
    domain_model: DomainModel
    contract_spec: ContractSpec

    def __init__(self, domain_model: DomainModel, contract_spec: ContractSpec):
        self.domain_model = domain_model
        self.contract_spec = contract_spec
    
    def to_sym(self):
        return f'\nDOMAIN MODEL:\n{self.domain_model.to_sym()}\n\nCONTRACTSPEC:\n{self.contract_spec.to_sym()}'

