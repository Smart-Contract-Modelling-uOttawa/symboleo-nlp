
class ILemmatize:
    def lemmatize(self, s: str) -> str:
        raise NotImplementedError()

class Lemmatizer(ILemmatize):
    def __init__(self, nlp):
        self.__nlp = nlp

    def lemmatize(self, s: str) -> str:
        doc = self.__nlp(s)
        return doc[0].lemma_
