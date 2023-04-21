from __future__ import annotations
from typing import List
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.helpers import SpecHelpers

class DeclarationProp:
    def __init__(self, key, value, type):
        self.key = key
        self.value = value
        self.type = type

    def __eq__(self, other: DeclarationProp) -> bool:
        return self.key == other.key and self.value == other.value and self.type == other.type
    
    def to_string(self):
        return f'{self.key} ({self.type}): {self.value}'

    def to_sym(self):
        return f'{self.key} := {self.value}'

class IDeclaration:
    name:str = None

    def to_obj(self):
        raise NotImplementedError()
    def to_sym(self):
        raise NotImplementedError()

# May eventually need to subtype this: Event, Role, Asset...
# nl_text - may need a more complex object for conjugation...
class Declaration(IDeclaration):
    def __init__(self, name: str, type: str, base_type:str, props: List[DeclarationProp], nl_text: str = ''):
        self.name = name
        self.type = type
        self.base_type = base_type # events, roles, assets 
        self.props = props
        self.nl_text = nl_text
    
    def __eq__(self, other: Declaration) -> bool:
        return self.base_type == other.base_type and \
            self.name == other.name and \
            self.type == other.type and \
            SpecHelpers.lists_eq(self.props, other.props, 'key')

    def to_obj(self):
        if self.base_type == 'events':
            return VariableEvent(self.name)
        
        return self.name

    def to_sym(self):
        result = f'{self.name}: {self.type}'
        if len(self.props) > 0:
            result += ' with '
        
        assnts_sym = ', '.join([x.to_sym() for x in self.props])
        result += assnts_sym
        result += ';'
        return result

