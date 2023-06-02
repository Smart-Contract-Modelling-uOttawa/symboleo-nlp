class ObligationSubject:
    def __init__(self, str_val: str):
        self.str_val = str_val

    def __eq__(self, __value: object) -> bool:
        return self.str_val == __value.str_val
    
    def to_text(self):
        return f'{self.str_val} obligation'