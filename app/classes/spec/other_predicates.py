from app.classes.spec.proposition import PAtom

class OtherFunction(PAtom):
    def to_sym(self):
        raise NotImplementedError()


class PredicateFunctionIsEqual(OtherFunction):
    def __init__(self, arg1: str, arg2: str):
        self.name = 'IsEqual'
        self.arg1 = arg1
        self.arg2 = arg2
    
    def to_sym(self):
        return f'{self.name}({self.arg1}, {self.arg2})'


class PredicateFunctionIsOwner(OtherFunction):
    def __init__(self, arg1:str, arg2:str):
        self.name = 'IsOwner'
        self.arg1 = arg1
        self.arg2 = arg2
    
    def to_sym(self):
        return f'{self.name}({self.arg1}, {self.arg2})'


class PredicateFunctionCannotBeAssigned(OtherFunction):
    def __init__(self, arg1):
        self.name = 'CannotBeAssigned'
        self.arg1 = arg1
    
    def to_sym(self):
        return f'{self.name}({self.arg1})'
