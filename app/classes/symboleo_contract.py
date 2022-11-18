from typing import Dict
from app.classes.domain_model.domain_model import Role, DomainEvent, Asset
from app.classes.spec.symboleo_spec import Obligation
from app.classes.spec.symboleo_spec import Power

class DomainModel:
    def __init__(
        self, 
        roles: Dict[str, Role], 
        events: Dict[str, DomainEvent], 
        assets: Dict[str, Asset]
    ):
        self.roles = roles
        self.events = events
        self.assets = assets
    
    def to_sym(self):
        result = '== Roles ==\n'
        for x in self.roles:
            result += f'{x}: {self.roles[x].to_sym()}\n'
        
        result += '\n== Assets ==\n'
        for x in self.assets:
            result += f'{x}: {self.assets[x].to_sym()}\n'
        
        result += '\n== Events ==\n'
        for x in self.events:
            result += f'{x}: {self.events[x].to_sym()}\n'
        
        return result


class ContractSpec:
    def __init__(
        self, 
        obligations: Dict[str, Obligation], 
        powers: Dict[str,Power]
    ):
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
    def __init__(
        self, 
        domain_model: DomainModel, 
        contract_spec: ContractSpec, 
        template_strings # TODO: Standardize this
    ):
        self.domain_model = domain_model
        self.contract_spec = contract_spec
        self.template_strings = template_strings
    
    def to_sym(self):
        return f'\nDOMAIN MODEL:\n{self.domain_model.to_sym()}\n\nCONTRACT SPEC:\n{self.contract_spec.to_sym()}'

