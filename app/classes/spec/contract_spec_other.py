class ContractSpecParameter:
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
    
    def to_sym(self):
        return f'{self.name}: {self.type}'
