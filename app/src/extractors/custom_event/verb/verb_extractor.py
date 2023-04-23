from app.classes.custom_event.verb import Verb, VerbType, VerbLists

from app.src.extractors.custom_event.verb.lemmatizer import ILemmatize
from app.src.extractors.custom_event.verb.conjugator import IConjugate

class IExtractVerb:
    def extract(self, verb_str: str) -> Verb:
        raise NotImplementedError()

class VerbExtractor:
    def __init__(
        self, 
        lemmatizer: ILemmatize,
        conjugator: IConjugate
    ):
        self.__lemmatizer = lemmatizer
        self.__conjugator = conjugator
    
    def extract(self, verb_str: str) -> Verb:
        self._validate(verb_str)

        lemma = self.__lemmatizer.lemmatize(verb_str)

        # May pull this out if needed
        verb_types = self._get_verb_types(lemma)

        conjugations = self.__conjugator.conjugate(lemma)        

        return Verb(verb_str, lemma, verb_types, conjugations)


    def _validate(self, verb_str: str):
        # Only allow single word (Limitation)
        if len(verb_str.split(' ')) > 1:
            raise ValueError('Verb can only be one word...for now')


    def _get_verb_types(self, lemma):
        result = []

        if lemma in VerbLists.intransitive_verbs:
            result.append(VerbType.INTRANSITIVE)
        if lemma in VerbLists.transitive_verbs:
            result.append(VerbType.TRANSITIVE)
        if lemma in VerbLists.linking_verbs:
            result.append(VerbType.LINKING)
        
        # If not in any, then add all of them
        if len(result) == 0:
            # Or maybe its an error?
            result = [VerbType.INTRANSITIVE, VerbType.TRANSITIVE, VerbType.LINKING]
        return result
