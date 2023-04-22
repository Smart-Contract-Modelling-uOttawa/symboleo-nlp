from __future__ import annotations
import copy
from typing import List
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
        self.is_alias = (base_type is not None)

        if self.is_alias:
            self.props = copy.deepcopy(base_type.props)
            self.base_type_name = base_type.name
        else:
            self.desc = desc
            self.props = props
    
    def to_obj(self):
        return self.name
    
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
    
    def __eq__(self, other: DomainObject) -> bool:
        return self.name == other.name and \
            ClassHelpers.lists_eq(self.props, other.props, 'key')


class Role(DomainObject):
    def __init__(self, name: str, props: List[DomainProp]):
        super().__init__('isA Role', name, props)
    
class Asset(DomainObject):
    def __init__(self, name: str, props: List[DomainProp], base_type: Asset = None):
        super().__init__('isAn Asset', name, props, base_type)
    
# TODO: Will replace the event_text with a template object - used for building new event instances
class DomainEvent(DomainObject):
    def __init__(self, name: str, props: List[DomainProp], event_text: str = ''):
        super().__init__('isAn Event', name, props)
        self.event_text = event_text
    
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
