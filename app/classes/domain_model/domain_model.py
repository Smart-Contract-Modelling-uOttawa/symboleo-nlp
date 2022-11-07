class DomainProp:
    def __init__(self, key, value, type):
        self.key = key
        self.value = value
        self.type = type

class Role:
    def __init__(self, name: str, props:list[DomainProp] = []):
        self.name = name
        self.props = props


class Asset:
    def __init__(self, name: str, parent:str, props:list[DomainProp] = []):
        self.name = name
        self.parent = parent
        self.props = props

class DomainEvent:
    def __init__(self, name:str, props:list[DomainProp] = []):
        self.name = name 
        self.props = props
