from typing import List

class Assignment:
    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value
    
    def to_sym(self):
        return f'{self.name} := {self.value}'


class ContractSpecParameter:
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
    
    def to_sym(self):
        return f'{self.name}: {self.type}'


class SymVariable:
    def __init__(self, id: str, type: str, assignments: List[Assignment]):
        self.id = id
        self.type = type
        self.assignments = assignments
    
    def to_sym(self):
        result = f'{self.id}: {self.type}'
        if len(self.assignments) > 0:
            result += ' with '
        
        assnts_sym = ', '.join([x.to_sym() for x in self.assignments])
        result += assnts_sym
        result += ';'
        return result
