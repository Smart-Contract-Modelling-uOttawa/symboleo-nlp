from spacy.tokens.span import Span

class IScoreSimilarity:
    def score(self, s1: Span, s2: Span) -> float:
        raise NotImplementedError()
    

# This is when I can incorporate things like wordnet as well to get a more precise score
# Can also go word by word and take some sort of max
## e.g. comparing "their warehouse" to "warehouse"...
class SimilarityScorer(IScoreSimilarity):
    def __init__(self, delta=0.25):
        self.__delta = delta

    def score(self, s1: Span, s2: Span):
        sim =  s1.similarity(s2) + self.__delta
        return min(1, sim)

