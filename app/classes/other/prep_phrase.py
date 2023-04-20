class PrepPhrase:
    def __init__(
        self, 
        pp_str: str,
        prepsition: str,
        pobj: str    
    ):
        self.pp_str = pp_str
        self.preposition = prepsition
        self.pobj = pobj
    
    def to_text(self):
        return self.pp_str
    