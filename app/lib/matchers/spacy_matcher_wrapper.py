from spacy.matcher import Matcher

class IWrapSpacyMatchers:
    def match(self, doc) -> list[tuple[str, int, int]]:
        raise NotImplementedError()

class SpacyMatcherWrapper(IWrapSpacyMatchers):
    def __init__(self, key, nlp, match_patterns):
        self.__nlp = nlp
        self.spacy_matcher = Matcher(nlp.vocab)
        self.spacy_matcher.add(key, [match_patterns])
    
    def match(self, doc) -> list[tuple[str, int, int]]:
        matches = self.spacy_matcher(doc)
        result = []
        for m in matches:
            ml = list(m)
            ml[0] = self.__nlp.vocab.strings[m[0]]
            result.append(tuple(ml))

        return result


