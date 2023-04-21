from app.classes.other.prep_phrase import PrepPhrase

from app.src.nlp.noun_phrase_extractor import IExtractNounPhrase

class IExtractPrepPhrase:
    def extract(self, pp_str: str) -> PrepPhrase:
        raise NotImplementedError()


# Examples
## with bob
## to the store
## could treat the pobj as a NP and use the subject extractor
## Would generalize the subjExtractor to be a NP Extractor
## Definitely possible without too much trouble. Can add as a feature later on
class PrepPhraseExtractor(IExtractPrepPhrase):    
    def __init__(self, nlp, np_extractor: IExtractNounPhrase):
        self.__nlp = nlp
        self.__np_extractor = np_extractor

    def extract(self, pp_str: str) -> PrepPhrase:
        # First identify the preposition and the pobj
        ## Start with a simple split
        ## Check if first word is ADP... Can also check a set of lists
        ## Might also want to integrate roles/assets as well...
        ## Or perhaps that is part of the options when it comes in nd not our concern...
        #doc = self.__nlp(pp_str)

        spl = pp_str.split(' ')

        preposition = spl[0]
        pobj_str = ' '.join(spl[1:])
        pobj = self.__np_extractor.extract(pobj_str)

        return PrepPhrase(pp_str, preposition, pobj)
