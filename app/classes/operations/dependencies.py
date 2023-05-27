from app.classes.spec.symboleo_contract import ISymboleoContract

class Dependencies:
    def __init__(self, nlp, fake: bool = False, use_new = True ):
        self.nlp = nlp
        self.fake = fake
        self.use_new = use_new


