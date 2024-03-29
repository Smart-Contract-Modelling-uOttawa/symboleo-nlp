from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.events.custom_event.prep_phrase import PrepPhrase
from app.classes.events.custom_event.noun_phrase import NounPhrase
from app.src.custom_event_extractor.element_extractor import IExtractElement

class PrepPhraseExtractor(IExtractElement[PrepPhrase]):    
    def __init__(self, np_extractor: IExtractElement[NounPhrase]):
        self.__np_extractor = np_extractor

    def extract(self, str_val: str, contract: SymboleoContract = None) -> PrepPhrase:
        spl = str_val.split(' ')

        # TODO: F2 - May want to verify that its a valid preposition. Can use NLP here...
        preposition = spl[0]

        pobj_str = ' '.join(spl[1:])
        pobj = self.__np_extractor.extract(pobj_str, contract)

        return PrepPhrase(str_val, preposition, pobj)
