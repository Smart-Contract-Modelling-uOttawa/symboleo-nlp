from __future__ import annotations

class ContractSpecParameter:
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
    
    def __eq__(self, other: ContractSpecParameter) -> bool:
        return self.name == other.name and self.type == other.type
    
    def to_sym(self):
        return f'{self.name}: {self.type}'
