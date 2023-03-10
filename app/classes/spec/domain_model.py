from __future__ import annotations
import copy
from typing import List
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.contract_spec_other import SymVariable, Assignment

class DomainProp:
    def __init__(self, key, value, type):
        self.key = key
        self.value = value
        self.type = type
    
    def to_sym(self):
        return f'{self.key}: {self.type}'


class DomainObject:
    def __init__(self, desc:str, name: str, props: List[DomainProp], base_type: DomainObject = None):
        self.name = name
        self.is_alias = (base_type is not None)

        if self.is_alias:
            self.props = copy.deepcopy(base_type.props)
            self.base_type_name = base_type.name
        else:
            self.desc = desc
            self.props = props
    
    def to_obj(self):
        return self.name

    def set_prop(self, prop_key, value):
        props = [x for x in self.props if x.key == prop_key]
        if len(props) != 1:
            raise KeyError(f'property {prop_key} not found')

        props[0].value = value
    

    # This will be used for an initialized DomainObject
    def to_declaration(self, decl_type) -> SymVariable:
        assnts = [Assignment(x.key, x.value,) for x in self.props]
        return SymVariable(self.name, decl_type, assnts)
    

    def to_sym(self):
        if self.is_alias:
            return f'{self.name} isA {self.base_type_name};'
        
        result = f'{self.name} {self.desc}'
        if len(self.props) > 0:
            result += ' with '
        
        props_sym = ', '.join([x.to_sym() for x in self.props])
        result += props_sym
        result += ';'

        return result


class Role(DomainObject):
    def __init__(self, name: str, props: List[DomainProp]):
        super().__init__('isA Role', name, props)
    
class Asset(DomainObject):
    def __init__(self, name: str, props: List[DomainProp], base_type: Asset = None):
        super().__init__('isAn Asset', name, props, base_type)
    
class DomainEvent(DomainObject):
    def __init__(self, name: str, props: List[DomainProp]):
        super().__init__('isAn Event', name, props)
    
    def to_obj(self):
        return VariableEvent(self.name)

class DomainEnum:
    def __init__(self, name:str, enum_items: List[str]):
        self.name = name
        self.enum_items = enum_items
    
    def to_sym(self):
        result = f'{self.name} isAn Enumeration'
        item_syms = ', '.join(self.enum_items)
        result += f'({item_syms});'
        return result
