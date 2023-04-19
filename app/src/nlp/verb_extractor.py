from app.src.helpers.string_to_class import CaseConverter

class Verb:
    # Maybe we can put an adverb in here... Or could put multiple
    # We may also build it with a set of conjugations...
    def __init__(self, lemma: str, adverb: str = None):
        self.lemma = lemma
        self.adverb = adverb
    
    def __eq__(self, other: object) -> bool:
        return self.lemma == other.lemma and self.adverb == other.adverb

    def print_me(self):
        print(f'- Lemma: {self.lemma}')
        print(f'- Adverb: {self.adverb}')

class IExtractVerb:
    def extract(self, evt: str) -> Verb:
        raise NotImplementedError()


class VerbExtractor:
    def __init__(self, nlp):
        self.__nlp = nlp
    
    def extract(self, evt: str) -> Verb:
        verb_txt = adverb_txt = None

        evt_snake = CaseConverter.to_snake(evt)
        if '_' in evt_snake:
            verb_txt, adverb_txt = evt_snake.split('_')
        else:
            verb_txt = evt_snake

        doc = self.__nlp(verb_txt)
        token = doc[0]
        lemma = token.lemma_

        adverb = None
        if adverb_txt:
            doc2 = self.__nlp(f'{verb_txt} {adverb_txt}')
            token = doc2[1]
            adverb = token.lemma_

        return Verb(lemma, adverb)


