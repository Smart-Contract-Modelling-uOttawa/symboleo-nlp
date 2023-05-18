import unittest
from unittest.mock import MagicMock
from app.classes.custom_event.prep_phrase import PrepPhrase
from app.classes.custom_event.noun_phrase import NounPhrase
from app.src.extractors.value_extractor import IExtractValue
from app.src.extractors.custom_event.prep_phrase_extractor import PrepPhraseExtractor

class PrepPhraseExtractorTests(unittest.TestCase):
    def setUp(self):
        self.nlp = None
        self.np_extractor = IExtractValue[NounPhrase]()
        self.sut = PrepPhraseExtractor(self.nlp, self.np_extractor)
    

    def test_pp_extractor(self):
        str_val = 'with a credit card'
        fake_np = NounPhrase('credit card', 'card', adjs=['credit'])
        self.np_extractor.extract = MagicMock(return_value=fake_np)

        result = self.sut.extract(str_val, None)

        expected = PrepPhrase(str_val, 'with', fake_np)
        self.assertEqual(result, expected)
        self.assertEqual(self.np_extractor.extract.call_count, 1)


if __name__ == '__main__':
    unittest.main()
