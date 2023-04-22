from app.classes.spec.symboleo_contract import ISymboleoContract

class Dependencies:
    def __init__(self, nlp, fake: bool = False):
        self.nlp = nlp
        self.fake = fake


