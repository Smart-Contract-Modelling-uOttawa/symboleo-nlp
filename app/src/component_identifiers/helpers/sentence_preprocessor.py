class IPreprocessSentences:
    def preprocess(self, doc):
        raise NotImplementedError()

class SentencePreprocessor(IPreprocessSentences):
    def __init__(self, nlp):
        self.__nlp = nlp

    def preprocess(self, doc):
        a = [x for x in doc if not x.is_stop]
        b = [x.lemma_ for x in a]
        return self.__nlp(' '.join(b))
        