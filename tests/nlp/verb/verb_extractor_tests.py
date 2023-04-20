
import unittest
from unittest.mock import MagicMock

from app.src.nlp.verb.lemmatizer import ILemmatize
from app.src.nlp.verb.conjugator import IConjugate

from app.classes.other.verb import VerbConjugations
from app.src.nlp.verb.verb_extractor import VerbExtractor

class VerbExtractorTests(unittest.TestCase):
    def setUp(self):
        lemmatizer = ILemmatize()
        lemmatizer.lemmatize = MagicMock(return_value='test')

        conjugator = IConjugate()
        fake_vc = VerbConjugations('a', 'b', 'c', 'd')
        conjugator.conjugate = MagicMock(return_value=fake_vc)
        self.sut = VerbExtractor(lemmatizer, conjugator)

    # Basic test
    def test_verb_extractor(self):
        result = self.sut.extract('test')
        self.assertEqual(result.lemma, 'test')
    
    # Fail validation
    def test_verb_extractor(self):
        with self.assertRaises(ValueError) as context:
            self.sut.extract('do something')

        self.assertTrue('one word' in str(context.exception))
    
if __name__ == '__main__':
    unittest.main()


