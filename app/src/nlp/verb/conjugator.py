from mlconjug3 import Conjugator as ML3Conjugator
from app.classes.other.verb import VerbConjugations

class IConjugate:
    def conjugate(self, lemma: str) -> VerbConjugations:
        raise NotImplementedError()

class MyConjugator(IConjugate):
    def __init__(self, mlconj: ML3Conjugator):
        self.__mlconj = mlconj

    def conjugate(self, lemma: str) -> VerbConjugations:
        verb = self.__mlconj.conjugate(lemma)

        pres_sing = verb['indicative']['indicative present']['I']
        pres_plur = verb['indicative']['indicative present']['he/she/it']
        past = verb['indicative']['indicative past tense']['I']
        continuous = verb['indicative']['indicative present continuous']['I']

        return VerbConjugations(
            present_singular=pres_sing,
            present_plural=pres_plur,
            past=past,
            continuous=continuous
        )