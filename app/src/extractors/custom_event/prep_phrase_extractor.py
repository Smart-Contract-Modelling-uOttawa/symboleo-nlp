from app.classes.custom_event.prep_phrase import PrepPhrase
from app.classes.custom_event.noun_phrase import NounPhrase
from app.src.extractors.value_extractor import IExtractValue

# TODO: More work needed here...
## Check if first word is ADP... Can also check a set of lists
## Might also want to integrate roles/assets as well...
## Or perhaps that is part of the options when it comes in nd not our concern...
class PrepPhraseExtractor(IExtractValue[PrepPhrase]):    
    def __init__(self, nlp, np_extractor: IExtractValue[NounPhrase]):
        self.__nlp = nlp
        self.__np_extractor = np_extractor

    def extract(self, str_val: str) -> PrepPhrase:
        spl = str_val.split(' ')

        preposition = spl[0]
        pobj_str = ' '.join(spl[1:])
        pobj = self.__np_extractor.extract(pobj_str)

        return PrepPhrase(str_val, preposition, pobj)
