from spacy.matcher import Matcher
from app.src.matchers.interfaces import IValidateMatches
from app.src.matchers.spacy_matcher_wrapper import IWrapSpacyMatchers

class SimpleValidator(IValidateMatches):
    def __init__(self, key, nlp, spacy_matcher_wrapper):
        self.__key = key
        self.__nlp = nlp
        self.__spacy_matcher_wrapper: IWrapSpacyMatchers = spacy_matcher_wrapper

    def validate(self, doc):
        matches = self.__spacy_matcher_wrapper.match(doc)
       
        if len(matches) != 1:
            return False
    
        sentence_type = matches[0][0]

        if sentence_type != self.__key:
            return False
        
        return True