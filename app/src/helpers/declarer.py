from typing import List
from app.classes.symboleo_contract import DomainModel
from app.classes.spec.domain_model import DomainObject
from app.classes.spec.declaration import Declaration, DeclarationProp

# Instantiate a declaration given DM info
class Declarer:
    @staticmethod
    def declare(dm: DomainModel, obj_type: str, obj_name: str, obj_key: str, props: List = []) -> Declaration:
        dm_obj: DomainObject = dm.__dict__[obj_type][obj_name]

        new_props: List[DeclarationProp] = []

        for k,v in props:
            find_props = [x for x in dm_obj.props if x.key == k]
            if len(find_props) != 1:
                raise KeyError(f'property {k} not found')
            found_prop = find_props[0]
        
            next_prop = DeclarationProp(k, v, found_prop.type)
            new_props.append(next_prop)

        return Declaration(obj_key, dm_obj.name, obj_type, new_props)


    @staticmethod
    def declare_input(domain_obj: DomainObject, base_type: str) -> Declaration:
        new_name = 'evt_' + domain_obj.name[0].lower() + domain_obj.name[1:]

        props: List[DeclarationProp] = []

        for dp in domain_obj.props:
            val = input(f'Enter value for {dp.key} ({dp.type}): ')
            # TODO: Validate type...
            # TODO: Give options, depending on the type (e.g. if Role, then must choose a Role)
            next_prop = DeclarationProp(dp.key, val, dp.type)
            props.append(next_prop)
        
        return Declaration(new_name, domain_obj.name, base_type, props)