from operator import itemgetter
from app.src.component_identifiers.helpers.similarity_calculator import ICalculateSentenceSimilarity

class IScoreVariables:
    def score(self, doc) -> tuple[str, float]:
        raise NotImplementedError()

# TODO: May incorporate other contrct elements here 
## e.g. the NL sentences (already done), the domain model, etc.
class VariableScorer(IScoreVariables):
    def __init__(
        self,
        nlp,
        sentence_dict,
        similarity_calculator: ICalculateSentenceSimilarity
    ):
        self.__nlp = nlp
        self.__sentence_dict = sentence_dict
        self.__similarity_calculator = similarity_calculator
    
    def score(self, doc) -> tuple[str, float]:
        res = []

        for key in self.__sentence_dict:
            test_sent = self.__sentence_dict[key]
            test_doc = self.__nlp(test_sent)
            similarity = self.__similarity_calculator.calculate(doc, test_doc)
            res.append((key, similarity))

        return max(res, key=itemgetter(1))