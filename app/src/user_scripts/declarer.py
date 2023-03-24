from typing import List
from app.classes.symboleo_contract import SymboleoContract, DomainModel
from app.classes.spec.domain_model import DomainObject
from app.classes.spec.declaration import Declaration, DeclarationProp


class ManualDeclarer:
    @staticmethod
    def declare_input(contract: SymboleoContract, domain_obj: DomainObject, base_type: str) -> Declaration:
        new_name = 'evt_' + domain_obj.name[0].lower() + domain_obj.name[1:]

        props: List[DeclarationProp] = []

        for dp in domain_obj.props:
            val = ManualDeclarer.get_input_by_type(contract, dp.key, dp.type)
            # TODO: Validate type...
            next_prop = DeclarationProp(dp.key, val, dp.type)
            props.append(next_prop)
        
        return Declaration(new_name, domain_obj.name, base_type, props)

    @staticmethod
    def get_input_by_type(contract: SymboleoContract, key: str, type_name:str):
        # Need to strongly type the types
        domain_model = contract.domain_model
        declarations = contract.contract_spec.declarations

        assets = [x.name for x in domain_model.assets.values()]
        roles = [x.name for x in domain_model.roles.values()]

        if type_name == 'String':
            val = input(f'Enter text for \'{key}\': ' )
        
        elif type_name == 'Date':
            val = input(f'Enter date for \'{key}\' (yyyy/mm/dd): ')
            # Can validate
        
        elif type_name == 'Number':
            val = input(f'Enter string for \'{key}\': ')
        
        elif type_name == 'Role':
            print(f'\nSelect value for \'{key}\' from the following roles:')
            val = ManualDeclarer._get_input_from_list(roles)
        
        elif type_name == 'Asset':
            print(f'\nSelect value for \'{key}\' from the following assets:')
            val = ManualDeclarer._get_input_from_list(assets)
        
        elif type_name in roles:
            select_list = [d.name for d in declarations.values() if d.type == type_name and d.base_type == 'roles']
            val = ManualDeclarer._get_input_from_list(select_list)

        elif type_name in assets:
            select_list = [d.name for d in declarations.values() if d.type == type_name and d.base_type == 'assets']
            val = ManualDeclarer._get_input_from_list(select_list)

        else:
            raise ValueError(f'Invalid prop type: {type_name}')
    
        return val



    @staticmethod
    def _get_input_from_list(my_list):
        if len(my_list) == 0:
            raise ValueError('List is empty!!')
        
        if len(my_list) == 1:
            print(f' --> {my_list[0]}')
            return my_list[0]
        
        # Have a case if its empty as well...

        for i,x in enumerate(my_list):
            print(f'{i+1}: {x}')

        k = int(input('Select #: '))
        result = my_list[k-1]
        return result
