from spacy.matcher import Matcher


class IValidateMatches:
    def validate(self, doc):
        raise NotImplementedError()


class MatchValidator(IValidateMatches):
    def __init__(self, matcher: Matcher):
        self.__matcher = Matcher

    def validate(self, doc):
        matches = self.__matcher(doc)
        if len(matches) == 0:
            raise ValueError('Value does not match expected pattern')

