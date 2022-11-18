from app.classes.spec.sym_event import VariableDotExpression, VariableEvent

class DomainProp:
    def __init__(self, key, value, type):
        self.key = key
        self.value = value
        self.type = type
    
    def to_sym(self):
        return f'{self.key} ({self.type}): {self.value}'

class Role:
    def __init__(self, name: str, props:list[DomainProp] = []):
        self.name = name
        self.props = props

    def to_obj(self):
        return VariableDotExpression(self.name)
    
    def to_sym(self):
        result = f'{self.name}\n'
        for x in self.props:
            result += f'- {x.to_sym()}\n'

        return result
    

class Asset:
    def __init__(self, name: str, parent:str = 'Asset', props:list[DomainProp] = []):
        self.name = name
        self.parent = parent
        self.props = props

    def to_sym(self):
        result = f'{self.name} ({self.parent})\n'
        for x in self.props:
            result += f'- {x.to_sym()}\n'
            
        return result


class DomainEvent:
    def __init__(self, name:str, props:list[DomainProp] = []):
        self.name = name 
        self.props = props
    
    def to_obj(self):
        return VariableEvent(VariableDotExpression(self.name))
    
    def to_sym(self):
        result = f'{self.name}\n'
        for x in self.props:
            result += f'- {x.to_sym()}\n'
            
        return result
