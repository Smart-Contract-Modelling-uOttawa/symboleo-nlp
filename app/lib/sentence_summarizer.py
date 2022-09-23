from nltk.tree import *
from spacy import displacy
from spacy.language import Language

class ISummarizeSentence:
    def summarize(self, sentence: str):
        raise NotImplementedError()

class SentenceSummarizer(ISummarizeSentence):
    def __init__(
        self,
        nlp):
        self.__nlp: Language = nlp

    def summarize(self, sentence: str):
        print(f'\nSentence: {sentence}\n')
        doc = self.__nlp(sentence)

        sent = list(doc.sents)[0]

        print(f'{"i":5} {"TEXT":15} {"POS":15} {"TAG":15} {"DEP":15} {"LEMMA":15} {"HEAD":15} {"ENT":15}')
        print('-----------'*10)
        for t in doc:
            print(f'{str(t.i):5} {t.text:15} {t.pos_:15} {t.tag_:15} {t.dep_:15} {t.lemma_:15} {t.head.text:15} {t.ent_type_:15}')

        print('\n\n')

        tree = Tree.fromstring(sent._.parse_string)
        tree.pretty_print()

        print('\n\n')

        displacy.render(doc, style="dep", jupyter=True)