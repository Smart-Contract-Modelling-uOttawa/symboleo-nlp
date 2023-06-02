from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.events.custom_event.prep_phrase import PrepPhrase
from app.classes.events.custom_event.noun_phrase import NounPhrase
from app.src.selection.element_extractors.value_extractor import IExtractValue

class PrepPhraseExtractor(IExtractValue[PrepPhrase]):    
    def __init__(self, nlp, np_extractor: IExtractValue[NounPhrase]):
        self.__nlp = nlp
        self.__np_extractor = np_extractor

    def extract(self, str_val: str, contract: SymboleoContract = None) -> PrepPhrase:
        spl = str_val.split(' ')

        # TODO: May want to verify that its a valid proposition. Can use NLP here...
        preposition = spl[0]

        pobj_str = ' '.join(spl[1:])
        pobj = self.__np_extractor.extract(pobj_str, contract)

        return PrepPhrase(str_val, preposition, pobj)
