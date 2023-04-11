from typing import List
from app.classes.spec.domain_model import DomainModel
from app.classes.spec.domain_object import DomainObject
from app.classes.spec.declaration import Declaration, DeclarationProp

# TODO: Make this a method on the symboleo contract
## Or more likely jsut a declaration_buidler
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
