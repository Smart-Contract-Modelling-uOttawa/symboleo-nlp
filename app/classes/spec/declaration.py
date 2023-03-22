from typing import List
from app.classes.spec.sym_event import VariableEvent

class DeclarationProp:
    def __init__(self, key, value, type):
        self.key = key
        self.value = value
        self.type = type
    
    def to_sym(self):
        return f'{self.key} := {self.value}'

# May eventually need to subtype this: Event, Role, Asset...
class Declaration:
    def __init__(self, name: str, type: str, base_type:str, props: List[DeclarationProp]):
        self.name = name
        self.type = type
        self.base_type = base_type # events, roles, assets 
        self.props = props
    
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

