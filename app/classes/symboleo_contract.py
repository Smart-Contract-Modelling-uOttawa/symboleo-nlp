from typing import Dict, List
from app.classes.spec.domain_model import Role, DomainEvent, Asset, DomainEnum, DomainObject
from app.classes.spec.contract_spec import Obligation
from app.classes.spec.contract_spec import Power
from app.classes.spec.proposition import Proposition
from app.classes.spec.contract_spec_other import ContractSpecParameter
from app.classes.spec.declaration import Declaration
from app.classes.nl_template import NLTemplate

class DomainModel:
    def __init__(
        self, 
        id: str,
        roles: Dict[str, Role], 
        enums: List[DomainEnum],
        events: Dict[str, DomainEvent], 
        assets: Dict[str, Asset]
    ):
        self.id = id
        self.roles = roles
        self.enums = enums
        self.events = events
        #self.aliases = aliases
        self.assets = assets
    
    def to_sym(self):
        result = f'Domain {self.id}\n'
        for x in self.roles:
            result += f'  {self.roles[x].to_sym()}\n'

        for x in self.enums:
            result += f'  {x.to_sym()}\n'

        for x in self.assets:
            result += f'  {self.assets[x].to_sym()}\n'

        for x in self.events:
            result += f'  {self.events[x].to_sym()}\n'

        result += f'\nendDomain'

        return result


class ContractSpec:
    def __init__(
        self, 
        id: str,
        parameters: List[ContractSpecParameter],
        declarations: Dict[str, Declaration],
        preconditions: List[Proposition],
        postconditions: List[Proposition],
        obligations: Dict[str, Obligation], 
        surviving_obligations: Dict[str, Obligation], 
        powers: Dict[str,Power],
        constraints: List[Proposition]
    ):
        self.id = id
        self.parameters = parameters
        self.declarations = declarations
        self.preconditions = preconditions
        self.postconditions = postconditions
        self.obligations = obligations
        self.surviving_obligations = surviving_obligations
        self.powers = powers
        self.constraints = constraints
    
    def to_sym(self):
        result = f'Contract {self.id}'
        parms_sym = ', '.join([x.to_sym() for x in self.parameters])
        result += f'( {parms_sym} )\n'


        result += '\nDeclarations\n'
        for x in self.declarations:
            result += f'  {self.declarations[x].to_sym()}\n'

        result += '\nPreconditions\n'
        for x in self.preconditions:
            result += f'  {x.to_sym()};\n'

        result += '\nPostconditions\n'
        for x in self.postconditions:
            result += f'  {x.to_sym()};\n'
        
        result += '\nObligations\n'
        for x in self.obligations:
            result += f'  {self.obligations[x].to_sym()}\n'
        
        result += '\nSurviving Obligations\n'
        for x in self.surviving_obligations:
            result += f'  {self.surviving_obligations[x].to_sym()}\n'

        result += '\nPowers\n'
        for x in self.powers:
            result += f'  {self.powers[x].to_sym()}\n'
        
        result += '\nConstraints\n'
        for x in self.constraints:
            result += f'  {x.to_sym()};\n'

        result += '\nendContract'
        return result


class SymboleoContract:
    def __init__(
        self, 
        domain_model: DomainModel, 
        contract_spec: ContractSpec, 
        nl_template: NLTemplate
    ):
        self.domain_model = domain_model
        self.contract_spec = contract_spec
        self.nl_template = nl_template

    # Print the NL template strings and their corresponding symboleo norms
    def print_all_strings(self):
        for x in self.nl_template.template_dict:
            val = self.nl_template.template_dict[x]
            print(f'{x}: {val.str_val}')

            mapping = val.mapping
            for m in mapping:
                t,v = m.split('.')
                norm = self.contract_spec.__dict__[t][v]
                print(f' - {norm.to_sym()}')
            print('\n')
    
    
    def to_sym(self):
        return f'{self.domain_model.to_sym()}\n\n{self.contract_spec.to_sym()}'

