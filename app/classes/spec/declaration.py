from __future__ import annotations
from typing import List
from enum import Enum
from app.classes.spec.sym_event import VariableEvent
from app.classes.events.custom_event.custom_event import CustomEvent
from app.classes.helpers.list_eq import ClassHelpers

class DeclarationType(Enum):
    ASSET = 'assets'
    ROLE = 'roles'
    EVENT = 'events'

class DeclarationProp:
    def __init__(self, key, value, type):
        self.key = key
        self.value = value
        self.type = type

    def __eq__(self, other: DeclarationProp) -> bool:
        return self.key == other.key and self.value == other.value and self.type == other.type
    
    def print_me(self):
        print(f'-- {self.key} ({self.type}): {self.value}')

    def to_string(self):
        return f'{self.key} ({self.type}): {self.value}'

    def to_sym(self):
        return f'{self.key} := {self.value}'

class IDeclaration:
    name:str = None

    def to_obj(self):
        raise NotImplementedError()
    def print_me(self):
        raise NotImplementedError()
    def to_sym(self):
        raise NotImplementedError()

class Declaration(IDeclaration):
    def __init__(self, name: str, type: str, base_type: DeclarationType, props: List[DeclarationProp] = None, id:str = None):
        self.id = id or name
        self.name = name
        self.type = type
        self.base_type = base_type # events, roles, assets 
        self.props = props or []
    
    def __eq__(self, other: Declaration) -> bool:
        return self.base_type == other.base_type and \
            self.id == other.id and \
            self.name == other.name and \
            self.type == other.type and \
            ClassHelpers.lists_eq(self.props, other.props, 'key')

    def to_obj(self):
        return self.name


    def print_me(self):
        print(f'\n- id: {self.id}')
        print(f'- name: {self.name}')
        print(f'- type: {self.type}')
        print(f'- base_type: {self.base_type}')
        for x in self.props:
            x.print_me()


    def to_sym(self):
        result = f'{self.id}: {self.type}'
        if len(self.props) > 0:
            result += ' with '
        
        assnts_sym = ', '.join([x.to_sym() for x in self.props])
        result += assnts_sym
        result += ';'
        return result



class EventDeclaration(Declaration):
    def __init__(self, name: str, type: str, props: List[DeclarationProp] = None, evt: CustomEvent = None):
        super().__init__(name, type, DeclarationType.EVENT.value, props)
        self.evt = evt
    
    def to_obj(self):
        return VariableEvent(self.name)
        
class AssetDeclaration(Declaration):
    def __init__(self, name: str, type: str, props: List[DeclarationProp] = None, id:str = None):
        super().__init__(name, type, DeclarationType.ASSET.value, props, id)

class RoleDeclaration(Declaration):
    def __init__(self, name: str, type: str, props: List[DeclarationProp] = None, id:str = None):
        super().__init__(name, type, DeclarationType.ROLE.value, props, id)