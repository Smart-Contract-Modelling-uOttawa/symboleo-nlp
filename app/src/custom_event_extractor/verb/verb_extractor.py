from app.classes.events.custom_event.verb import Verb, VerbType

from app.classes.units.unit_type import UnitType
from app.src.custom_event_extractor.nlp.lemmatizer import ILemmatize
from app.src.custom_event_extractor.verb.conjugator import IConjugate

from app.src.custom_event_extractor.element_extractor import IExtractElement

class IExtractVerb:
    def extract(self, str_val: str, unit_type: UnitType) -> Verb:
        raise NotImplementedError()

class VerbExtractor(IExtractElement[Verb]):
    def __init__(
        self, 
        lemmatizer: ILemmatize,
        conjugator: IConjugate
    ):
        self.__lemmatizer = lemmatizer
        self.__conjugator = conjugator
        self.__type_dict = {
            UnitType.TRANSITIVE_VERB: VerbType.TRANSITIVE,
            UnitType.INTRANSITIVE_VERB: VerbType.INTRANSITIVE,
            UnitType.LINKING_VERB: VerbType.LINKING
        }
    
    def extract(self, str_val: str, unit_type: UnitType) -> Verb:
        self._validate(str_val)

        lemma = self.__lemmatizer.lemmatize(str_val)

        # May pull this out if needed

        verb_type = self.__type_dict[unit_type]

        conjugations = self.__conjugator.conjugate(lemma)        

        return Verb(str_val, lemma, verb_type, conjugations)


    def _validate(self, verb_str: str):
        # Only allow single word (Limitation)

        if len(verb_str.split(' ')) > 1:
            raise ValueError('Verb can only be one word...for now')

