from __future__ import annotations
from typing import List
from app.classes.spec.sym_event import VariableEvent
from app.classes.custom_event.custom_event import CustomEvent
from app.classes.other.helpers import ClassHelpers

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

# TODO: Subclass the declaration types (assets, events, roles)
# TODO: Add evt init onto all Declaration constructors
class Declaration(IDeclaration):
    def __init__(self, name: str, type: str, base_type:str, props: List[DeclarationProp], evt: CustomEvent = None):
        self.name = name
        self.type = type
        self.base_type = base_type # events, roles, assets 
        self.props = props
        self.evt = evt # Will only appear on the events one
        # The evt will be needed for obligation events (e.g. fulfilling/violatin obligation)
    
    def __eq__(self, other: Declaration) -> bool:
        return self.base_type == other.base_type and \
            self.name == other.name and \
            self.type == other.type and \
            ClassHelpers.lists_eq(self.props, other.props, 'key')

    # TODO: Where is this used... need to extend it..
    def to_obj(self):
        if self.base_type == 'events':
            return VariableEvent(self.name)
        
        return self.name


    def print_me(self):
        print(f'\n- name: {self.name}')
        print(f'- type: {self.type}')
        print(f'- base_type: {self.base_type}')
        for x in self.props:
            x.print_me()


    def to_sym(self):
        result = f'{self.name}: {self.type}'
        if len(self.props) > 0:
            result += ' with '
        
        assnts_sym = ', '.join([x.to_sym() for x in self.props])
        result += assnts_sym
        result += ';'
        return result

