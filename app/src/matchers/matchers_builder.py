from app.src.matchers.interfaces import IMatcher
from app.src.matchers.simple.simple_matcher import SimpleMatcher
from app.src.matchers.simple.simple_validator import SimpleValidator
from app.src.matchers.spacy_matcher_wrapper import SpacyMatcherWrapper

from app.src.matchers.match_patterns import match_patterns

class MatchersBuilder:
    def __init__(self, nlp):
        self.__nlp = nlp 

    def build(self) -> list[IMatcher]:
        # Simple matching
        simple_matcher = MatchersBuilder.build_simple_matcher(self.__nlp)

        # Other matching...

        return [
            simple_matcher,
        ]

    @staticmethod
    def build_simple_matcher(nlp):
        simple_key = 'simple'
        simple_match_patterns = match_patterns[simple_key]
        simple_sm_wrapper = SpacyMatcherWrapper(simple_key, nlp, simple_match_patterns)
        simple_validator = SimpleValidator(simple_key, nlp, simple_sm_wrapper)
        simple_matcher = SimpleMatcher(simple_key, nlp, simple_validator)
        return simple_matcher
        