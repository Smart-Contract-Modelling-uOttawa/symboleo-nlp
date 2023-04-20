from app.src.helpers.string_to_class import CaseConverter
from app.classes.other.verb import Verb, VerbType

from app.src.nlp.verb.verb_lists import VerbLists
from app.src.nlp.verb.lemmatizer import ILemmatize
from app.src.nlp.verb.conjugator import IConjugate

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

        verb_types = self._get_verb_types(lemma)

        conjugations = self.__conjugator.conjugate(verb_str)        

        return Verb(verb_str, lemma, verb_types, conjugations)


    def _validate(self, verb_str: str):
        # Only allow single word (Limitation)
        if len(verb_str.split(' ')) > 1:
            raise ValueError('Verb can only be one word...for now')


    # These were generated using ChatGPT (Limitation) - not perfect
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


