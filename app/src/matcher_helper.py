from spacy.matcher import Matcher

class IGetMatches:
    def match(self, pattern, doc): # returns a span
        raise NotImplementedError()
    

class MyMatcher(IGetMatches):
    def __init__(self, nlp):
        self.__nlp = nlp


    # Returns a span
    def match(self, pattern, doc):
        pattern_name = 'P'
        matcher = Matcher(self.__nlp.vocab)

        matcher.add(pattern_name, pattern)

        matches = matcher(doc)

        max_match = self._get_max_match(matches, pattern_name)

        if max_match:
            return doc[max_match[1]:max_match[2]]
        else:
            return None


    
    def _get_max_match(self, matches, pattern_name):
        all_matches = [x for x in matches if self.__nlp.vocab.strings[x[0]] == pattern_name]
        if len(all_matches) > 0:
            return max(all_matches, key=lambda x: x[2]-x[1])
        else:
            return None