from mlconjug3 import Conjugator as ML3Conjugator
from app.src.extractors.custom_event.verb.lemmatizer import Lemmatizer
from app.src.extractors.custom_event.verb.fake_lemmatizer import FakeLemmatizer
from app.src.extractors.custom_event.verb.conjugator import MyConjugator
from app.src.extractors.custom_event.verb.verb_extractor import VerbExtractor

class VerbExtractorBuilder:
    @staticmethod 
    def build(nlp, fake:bool=False):
        inner_conjugator = ML3Conjugator(language = 'en')
        if fake:
            lemmatizer = FakeLemmatizer()
        else:
            lemmatizer = Lemmatizer(nlp)
        
        conjugator = MyConjugator(inner_conjugator)
        return VerbExtractor(lemmatizer, conjugator)
