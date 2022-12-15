from app.src.component_identifiers.helpers.sentence_preprocessor import IPreprocessSentences


class ICalculateSentenceSimilarity:
    def calculate(self, doc1, doc2) -> float:
        raise NotImplementedError()

class SentenceSimilarityCalculator(ICalculateSentenceSimilarity):
    def __init__(
        self,
        preprocessor: IPreprocessSentences
    ):
        self.__preprocessor = preprocessor
    
    def calculate(self, doc1, doc2) -> float:
        d1 = self.__preprocessor.preprocess(doc1)
        d2 = self.__preprocessor.preprocess(doc2)
        sim = d1.similarity(d2)
        return round(sim, 3)