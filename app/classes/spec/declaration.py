from typing import List
from app.classes.spec.sym_event import VariableEvent

class DeclarationProp:
    def __init__(self, key, value, type):
        self.key = key
        self.value = value
        self.type = type
    
    def to_sym(self):
        return f'{self.key} := {self.value}'

class IDeclaration:
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

