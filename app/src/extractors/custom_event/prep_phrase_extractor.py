from app.classes.custom_event.prep_phrase import PrepPhrase

from app.src.extractors.custom_event.noun_phrase_extractor import IExtractNounPhrase

# TODO: More work todo here...
## Check if first word is ADP... Can also check a set of lists
## Might also want to integrate roles/assets as well...
## Or perhaps that is part of the options when it comes in nd not our concern...
class IExtractPrepPhrase:
    def extract(self, pp_str: str) -> PrepPhrase:
        raise NotImplementedError()

class PrepPhraseExtractor(IExtractPrepPhrase):    
    def __init__(self, nlp, np_extractor: IExtractNounPhrase):
        self.__nlp = nlp
        self.__np_extractor = np_extractor

    def extract(self, pp_str: str) -> PrepPhrase:
        spl = pp_str.split(' ')

        preposition = spl[0]
        pobj_str = ' '.join(spl[1:])
        pobj = self.__np_extractor.extract(pobj_str)

        return PrepPhrase(pp_str, preposition, pobj)
