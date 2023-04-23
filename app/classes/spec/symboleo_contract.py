from app.classes.spec._sd import _sd
from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.domain_model import DomainModel
from app.classes.spec.domain_object import Role, DomainEvent, Asset, DomainObject, DomainProp
from app.classes.spec.norm import INorm, Obligation, Norm
from app.classes.spec.proposition import PNegAtom, PAnd
from app.classes.spec.p_atoms import PAtomPredicate, PAtomPredicateFalseLiteral, PAtomPredicateTrueLiteral
from app.classes.spec.predicate_function import PredicateFunction, PredicateFunctionHappens
from app.classes.spec.contract_spec_parameter import ContractSpecParameter
from app.classes.spec.declaration import Declaration
from app.classes.spec.nl_template import NLTemplate, TemplateObj

from app.classes.operations.contract_update_obj import ContractUpdateObj


# XText link: https://github.com/Smart-Contract-Modelling-uOttawa/Symboleo-IDE/blob/master/ca.uottawa.csmlab.symboleo/src/ca/uottawa/csmlab/symboleo/Symboleo.xtext


class ISymboleoContract:
    def to_sym(self):
        raise NotImplementedError()
    def add_declaration(self, declaration: Declaration):
        raise NotImplementedError()
    def add_norm(self, norm: Norm, norm_key: str, norm_nl: str):
        raise NotImplementedError()
    def update_norm(self, norm: Norm, norm_component: str, pred: PredicateFunction, key: str, nl: str):
        raise NotImplementedError()
    def add_dm_object(self, dmo: DomainObject):
        raise NotImplementedError()
    def add_dm_prop(self, domain_prop: DomainProp, obj_type: str, obj_key:str):
        raise NotImplementedError()
    def get_norm(self, norm_id: str, norm_type:str) -> Norm:
        raise NotImplementedError()
    
    def get_norm_by_key(self, key:str):
        raise NotImplementedError()
    def run_updates(self, update: ContractUpdateObj):
        raise NotImplementedError()
    def update_nl(self, key, nl):
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

    def _get_type_key(self, type_str):
        d = {
            'Obligation': 'obligations',
            'Power': 'powers',
            'SO': 'surviving_obligations'
        }

        return d[type_str]
    

    def get_norm_by_key(self, key:str) -> INorm:
        mapping = self.nl_template.template_dict[key].mapping[0]
        norm_type, norm_id = mapping.split('.')
        result: Norm = self.contract_spec.__dict__[norm_type][norm_id]
        return result
    
    def run_updates(self, update: ContractUpdateObj):
        for x in update.domain_objects:
            self.add_dm_object(x) # Might make this internal

        for x in update.declarations:
            self.add_declaration(x) # Might make this internal

        for x in update.norms:
            self._update_norm(x)

    def _update_norm(self, norm: INorm):
        type_key = self._get_type_key(norm.norm_type.value)
        self.contract_spec.__dict__[type_key][norm.id] = norm

    def update_nl(self, key, nl): # Might include component check...
        t = self.nl_template.template_dict
        old_str = t[key].str_val
        new_nl = old_str + ' ' + nl
        t[key].str_val =  new_nl


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
        self._sort()
        return f'{self.domain_model.to_sym()}\n\n{self.contract_spec.to_sym()}'


    def add_declaration(self, declaration: Declaration):
        # Add the declaration
        self.contract_spec.declarations[declaration.name] = declaration

        # Add any new parameters as well
        parm_names = [x.name for x in self.contract_spec.parameters]
        decl_keys = [x for x in self.contract_spec.declarations]
        for dp in declaration.props:
            if dp.value not in parm_names and dp.value not in decl_keys:
                new_parm = ContractSpecParameter(dp.value, dp.type)
                self.contract_spec.parameters.append(new_parm)


    def update_norm(self, norm: Norm, norm_component: str, pred: PredicateFunction, key: str, nl: str):
        norm.update(norm_component, pred)

        t = self.nl_template.template_dict
        old_str = t[key].str_val
        
        if norm_component == 'trigger':
            new_nl = nl + ' ' + old_str
        else:
            new_nl = old_str + ' ' + nl
        
        t[key].str_val =  new_nl
        

    # May eventually just add a norm.nl property that corresponds to the nl
    def add_norm(self, norm: Norm, norm_key: str, norm_nl: str):
        norm_type = 'obligations' if type(norm) == Obligation else 'powers'
        self.contract_spec.__dict__[norm_type][norm.id] = norm

        t = self.nl_template.template_dict
        next_mapping = f'{norm_type}.{norm.id}'
        if norm_key in t:
            t[norm_key].mapping.append(next_mapping)
            t[norm_key].str_val += norm_nl # This will require some finessing...
        else:
            t[norm_key] = TemplateObj(norm_nl, [next_mapping])
    

    def add_dm_object(self, dmo: DomainObject):
        dm_dict = {
            DomainEvent: 'events',
            Asset: 'assets',
            Role: 'roles'
        }
        obj_type = dm_dict[type(dmo)]

        # Check to make sure it doesnt already exist...
        # If it exists, then maybe we just replace it ???
        if dmo.name not in self.domain_model.__dict__[obj_type]:
            self.domain_model.__dict__[obj_type][dmo.name] = dmo


    # Need domain prop updater...Might need to treat this differently
    def add_dm_prop(self, domain_prop: DomainProp, obj_type: str, obj_key:str):
        self.domain_model.__dict__[obj_type][obj_key].props.append(domain_prop)


    def get_norm(self, norm_id: str, norm_type:str) -> Norm:
        result: Norm = self.contract_spec.__dict__[norm_type][norm_id]
        return result
    
    def _sort(self):
        self.contract_spec.obligations = _sd(self.contract_spec.obligations)
        self.contract_spec.powers = _sd(self.contract_spec.powers)
        self.contract_spec.declarations = _sd(self.contract_spec.declarations)
        self.contract_spec.parameters = sorted(self.contract_spec.parameters, key=lambda x: x.name)
        self.contract_spec.surviving_obligations = _sd(self.contract_spec.surviving_obligations)

        self.domain_model.roles = _sd(self.domain_model.roles)
        self.domain_model.events = _sd(self.domain_model.events)
        self.domain_model.assets = _sd(self.domain_model.assets)
        self.domain_model.enums = sorted(self.domain_model.enums, key=lambda x: x.name)