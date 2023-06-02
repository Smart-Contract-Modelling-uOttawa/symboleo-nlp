from app.classes.events.custom_event.noun_phrase import NounPhrase

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
    
    def __eq__(self, __value: object) -> bool:
        return self.pp_str == __value.pp_str and \
            self.preposition == __value.preposition and \
            self.pobj == __value.pobj

    def to_text(self):
        return f'{self.preposition} {self.pobj.to_text()}'
    