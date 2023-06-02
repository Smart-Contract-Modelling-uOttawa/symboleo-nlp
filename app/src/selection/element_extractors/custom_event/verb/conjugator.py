from mlconjug3 import Conjugator as ML3Conjugator
from app.classes.events.custom_event.verb import VerbConjugations

class IConjugate:
    def conjugate(self, lemma: str) -> VerbConjugations:
        raise NotImplementedError()

class MyConjugator(IConjugate):
    def __init__(self, mlconj: ML3Conjugator):
        self.__mlconj = mlconj

    def conjugate(self, lemma: str) -> VerbConjugations:
        verb = self.__mlconj.conjugate(lemma)

        # ML3Conjugator: https://pypi.org/project/mlconjug3/
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
