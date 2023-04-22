class ObligationSubject:
    def __init__(self, str_val: str):
        self.str_val = str_val
    
    def to_text(self):
        return f'{self.str_val} obligation'