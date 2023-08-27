from __future__ import annotations
from typing import List
from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.domain_model import DomainModel
from app.classes.spec.domain_object import Role, DomainEvent, Asset, DomainObject
from app.classes.spec.norm import INorm, Norm
from app.classes.spec.norm_config import NormConfig
from app.classes.spec.contract_spec_parameter import ContractSpecParameter
from app.classes.spec.declaration import Declaration
from app.classes.spec.nl_template import NLTemplate

from app.classes.operations.contract_update_obj import ContractUpdateObj

# XText link: https://github.com/Smart-Contract-Modelling-uOttawa/Symboleo-IDE/blob/master/ca.uottawa.csmlab.symboleo/src/ca/uottawa/csmlab/symboleo/Symboleo.xtext

class ISymboleoContract:
    def to_sym(self):
        raise NotImplementedError()
    def get_norm_configs_by_key(self, nl_key: str, parm_key: str) -> List[NormConfig]:
        raise NotImplementedError()
    def run_updates(self, update: ContractUpdateObj):
        raise NotImplementedError()
    def update_nl(self, nl_key: str, parm_key: str, nl_refinement: str):
        raise NotImplementedError()


class SymboleoContract(ISymboleoContract):
    def __init__(
        self, 
        domain_model: DomainModel, 
        contract_spec: ContractSpec, 
        nl_template: NLTemplate
    ):
        self.domain_model = domain_model
        self.contract_spec = contract_spec
        self.nl_template = nl_template

    def to_sym(self):
        return f'{self.domain_model.to_sym()}\n\n{self.contract_spec.to_sym()}'
    

    def get_norm_configs_by_key(self, nl_key: str, parm_key: str) -> List[NormConfig]:
        results = []
        
        parm_configs = self.nl_template.template_dict[nl_key].parameters[parm_key]

        for parm_config in parm_configs:
            norm_type = parm_config.norm_type
            norm_id = parm_config.norm_id
            next_norm: Norm = self.contract_spec.__dict__[norm_type][norm_id]
            next_nc = NormConfig(next_norm, parm_config)
            results.append(next_nc)
        
        return results

    def run_updates(self, update: ContractUpdateObj):
        for x in update.domain_objects:
            self._add_dm_object(x) # Might make this internal

        for x in update.declarations:
            self._add_declaration(x) # Might make this internal

        for x in update.contract_parms:
            self._add_contract_parm(x)

        for x in update.norms:
            self._update_norm(x)

    def update_nl(self, nl_key: str, parm_key: str, nl_refinement: str):        
        t = self.nl_template.template_dict
        old_str = t[nl_key].str_val
        t[nl_key].str_val = old_str.replace(f'[{parm_key}]', nl_refinement)

        # Mark the parm as being filled
        for pc in t[nl_key].parameters[parm_key]:
            pc.filled = True

    def __eq__(self, other: SymboleoContract) -> bool:
        return self.domain_model == other.domain_model and \
            self.contract_spec == other.contract_spec and \
            self.nl_template == other.nl_template

    def _get_type_key(self, type_str):
        d = {
            'Obligation': 'obligations',
            'Power': 'powers',
            'SO': 'surviving_obligations'
        }
        return d[type_str]
    

    def _update_norm(self, norm: INorm):
        type_key = self._get_type_key(norm.norm_type.value)
        self.contract_spec.__dict__[type_key][norm.id] = norm


    def _add_contract_parm(self, csp: ContractSpecParameter):
        # Add any new parameters 
        parm_names = [x.name for x in self.contract_spec.parameters]

        if csp.name not in parm_names:
            self.contract_spec.parameters.append(csp)

    def _add_declaration(self, declaration: Declaration):
        # Add the declaration
        self.contract_spec.declarations[declaration.name] = declaration       
            

    def _add_dm_object(self, dmo: DomainObject):
        dm_dict = {
            DomainEvent: 'events',
            Asset: 'assets',
            Role: 'roles'
        }
        obj_type = dm_dict[type(dmo)]

        self.domain_model.__dict__[obj_type][dmo.name] = dmo

    # Print the NL template strings and their corresponding symboleo norms
    def print_all_strings(self): # pragma: no cover
        for x in self.nl_template.template_dict:
            val = self.nl_template.template_dict[x]
            print(f'{x}: {val.str_val}')
            print('\n')


    