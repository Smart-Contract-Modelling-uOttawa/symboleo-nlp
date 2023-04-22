from app.classes.custom_event.noun_phrase import NounPhrase

class PrepPhrase:
    def __init__(
        self, 
        pp_str: str,
        preposition: str,
        pobj: NounPhrase    
    ):
        self.pp_str = pp_str
        self.preposition = preposition
        self.pobj = pobj
    
    def to_text(self):
        return f'{self.preposition} {self.pobj.to_text()}'
    