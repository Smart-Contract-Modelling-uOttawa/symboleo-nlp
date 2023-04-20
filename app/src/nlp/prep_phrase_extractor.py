from app.classes.other.prep_phrase import PrepPhrase

class IExtractSubjectPrepPhrase:
    def extract(self, pp_str: str) -> PrepPhrase:
        raise NotImplementedError()


class PrepPhraseExtractor:    
    def __init__(self):
        self.__nlp = None

    def extract(self, pp_str: str) -> PrepPhrase:
        return PrepPhrase(pp_str)
