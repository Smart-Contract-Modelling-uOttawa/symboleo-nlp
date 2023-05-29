from __future__ import annotations
import copy
from typing import List, Tuple
from string import Template
from app.classes.spec.sym_event import VariableEvent
from app.classes.other.helpers import ClassHelpers

class DomainProp:
    def __init__(self, key, type):
        self.key = key
        self.type = type
    
    def to_sym(self):
        return f'{self.key}: {self.type}'
    
    def __eq__(self, other: DomainProp) -> bool:
        return self.key == other.key and self.type == other.type


class IDomainObject:
    def to_obj(self):
        raise NotImplementedError()
    def to_sym(self):
        raise NotImplementedError()
    


class DomainObject(IDomainObject):
    def __init__(self, desc:str, name: str, props: List[DomainProp], base_type: DomainObject = None):
        self.name = name
        self.base_type = base_type
        self.is_alias = (base_type is not None)

        if self.is_alias:
            self.props = props
            self.base_type_name = base_type.name
        else:
            self.desc = desc
            self.props = props
    
    def __eq__(self, other: DomainObject) -> bool:
        return self.name == other.name and \
            ClassHelpers.lists_eq(self.props, other.props, 'key')
    
    def to_obj(self):
        return self.name
    
    def to_sym(self):
        if self.is_alias:
            result =  f'{self.name} isA {self.base_type_name}'
        else:
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
    
  
# TODO: Will eventually want a way to build this in the new_event_updater code
## i.e. the declaration_to_domain mapper
class EventNLTemplate:
    def __init__(self, t: Template):
        self.t = t
        
    def render(self, arg_vals: List[Tuple[str,str]]):
        m = {i[0]: i[1] for i in arg_vals}
        return self.t.substitute(**m)

class DomainEvent(DomainObject):
    def __init__(self, name: str, props: List[DomainProp], event_template: EventNLTemplate = None):
        super().__init__('isAn Event', name, props)
        self.event_template = event_template
    
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
