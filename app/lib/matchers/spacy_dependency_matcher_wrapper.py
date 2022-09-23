from spacy.matcher import DependencyMatcher

class IWrapSpacyDependencyMatchers:
    def match(self, doc):
        raise NotImplementedError()

class SpacyDependencyMatcherWrapper(IWrapSpacyDependencyMatchers):
    def __init__(self, nlp, match_patterns):
        self.__nlp = nlp
        self.spacy_matcher = DependencyMatcher(nlp.vocab)
        for k in match_patterns:
            self.spacy_matcher.add(k, [match_patterns[k]])

    def match(self, doc):
        matches = self.spacy_matcher(doc)
        return matches

        # # Validate the match
        # sentence_type_id, match_tokens = matches[0]
        # sentence_type = self.__nlp.vocab.strings[sentence_type_id]

        # return DependencyMatch(
        #     sentence_type,
        #     match_tokens
        # )