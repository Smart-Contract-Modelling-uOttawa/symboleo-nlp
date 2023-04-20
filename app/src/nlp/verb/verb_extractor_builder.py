from mlconjug3 import Conjugator as ML3Conjugator
from app.src.nlp.verb.lemmatizer import Lemmatizer
from app.src.nlp.verb.conjugator import MyConjugator
from app.src.nlp.verb.verb_extractor import VerbExtractor

class VerbExtractorBuilder:
    @staticmethod 
    def build(nlp):
        inner_conjugator = ML3Conjugator(language = 'en')
        lemmatizer = Lemmatizer(nlp)
        conjugator = MyConjugator(inner_conjugator)
        return VerbExtractor(lemmatizer, conjugator)

