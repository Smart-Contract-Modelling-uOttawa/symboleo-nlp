from app.classes.custom_event.verb import Verb, VerbType, VerbLists

from app.classes.spec.symboleo_contract import SymboleoContract
from app.src.extractors.custom_event.verb.lemmatizer import ILemmatize
from app.src.extractors.custom_event.verb.conjugator import IConjugate

from app.src.extractors.value_extractor import IExtractValue


class VerbExtractor(IExtractValue[Verb]):
    def __init__(
        self, 
        lemmatizer: ILemmatize,
        conjugator: IConjugate
    ):
        self.__lemmatizer = lemmatizer
        self.__conjugator = conjugator
    
    def extract(self, str_val: str, contract: SymboleoContract = None) -> Verb:
        self._validate(str_val)

        # Check for negation?

        lemma = self.__lemmatizer.lemmatize(str_val)

        # May pull this out if needed
        verb_types = self._get_verb_types(lemma)

        conjugations = self.__conjugator.conjugate(lemma)        

        return Verb(str_val, lemma, verb_types, conjugations)


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
