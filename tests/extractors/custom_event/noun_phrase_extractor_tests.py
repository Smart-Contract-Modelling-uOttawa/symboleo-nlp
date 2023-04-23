import unittest
from unittest.mock import MagicMock
from app.classes.custom_event.noun_phrase import NounPhrase
from app.src.extractors.custom_event.noun_phrase_extractor import NounPhraseExtractor


# TODO: Organize the NPExtractor better, and make a fakeNLP to inject
## Or rather a simpler interface to the NLP
class NounPhraseExtractorTests(unittest.TestCase):
    def setUp(self):
        self.nlp = None
        self.sut = NounPhraseExtractor(self.nlp)
    
    @unittest.skip('TODO...')
    def test_noun_phrase_extractor(self):
        return
        

if __name__ == '__main__':
    unittest.main()
