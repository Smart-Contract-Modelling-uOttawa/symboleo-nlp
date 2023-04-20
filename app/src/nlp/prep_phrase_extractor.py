from app.classes.other.prep_phrase import PrepPhrase

class IExtractSubjectPrepPhrase:
    def extract(self, pp_str: str) -> PrepPhrase:
        raise NotImplementedError()


# Examples
## with bob
## to the store
## could treat the pobj as a NP and use the subject extractor
## Would generalize the subjExtractor to be a NP Extractor
## Definitely possible without too much trouble. Can add as a feature later on
class PrepPhraseExtractor:    
    def __init__(self, nlp):
        self.__nlp = nlp

    def extract(self, pp_str: str) -> PrepPhrase:
        # First identify the preposition and the pobj
        ## Start with a simple split
        ## Check if first word is ADP... Can also check a set of lists
        ## Might also want to integrate roles/assets as well...
        ## Or perhaps that is part of the options when it comes in nd not our concern...
        #doc = self.__nlp(pp_str)

        spl = pp_str.split(' ')

        preposition = spl[0]
        pobj = ' '.join(spl[1:])


        return PrepPhrase(pp_str, preposition, pobj)
