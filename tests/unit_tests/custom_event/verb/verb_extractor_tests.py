import unittest
from unittest.mock import MagicMock
from app.classes.events.custom_event.verb import Verb, VerbType, VerbConjugations
from app.src.selection.element_extractors.custom_event.verb.verb_extractor import VerbExtractor
from app.src.selection.element_extractors.custom_event.verb.lemmatizer import ILemmatize
from app.src.selection.element_extractors.custom_event.verb.conjugator import IConjugate


class VerbExtractorTests(unittest.TestCase):
    def setUp(self):
        self.lemmatizer = ILemmatize()
        self.conjugator = IConjugate()
        self.sut = VerbExtractor(self.lemmatizer, self.conjugator)
    


    def test_verb_extractor_transitive(self):
        self.lemmatizer.lemmatize = MagicMock(return_value='request')
        fake_conj = VerbConjugations('a', 'b', 'c', 'd')
        self.conjugator.conjugate = MagicMock(return_value=fake_conj)
        str_val = 'requests'
        result = self.sut.extract(str_val)
        expected = Verb(str_val, 'request', [VerbType.TRANSITIVE], fake_conj)
        
        self.assertEqual(result, expected)
        self.assertEqual(self.lemmatizer.lemmatize.call_count, 1)
        self.assertEqual(self.conjugator.conjugate.call_count, 1)
    
    
    def test_verb_extractor_linking(self):
        self.lemmatizer.lemmatize = MagicMock(return_value='become')
        fake_conj = VerbConjugations('a', 'b', 'c', 'd')
        self.conjugator.conjugate = MagicMock(return_value=fake_conj)
        str_val = 'become'
        result = self.sut.extract(str_val)
        expected = Verb(str_val, 'become', [VerbType.LINKING], fake_conj)
        
        self.assertEqual(result, expected)
        self.assertEqual(self.lemmatizer.lemmatize.call_count, 1)
        self.assertEqual(self.conjugator.conjugate.call_count, 1)
    

    def test_verb_extractor_3(self):
        self.lemmatizer.lemmatize = MagicMock(return_value='terminate')
        fake_conj = VerbConjugations('a', 'b', 'c', 'd')
        self.conjugator.conjugate = MagicMock(return_value=fake_conj)
        str_val = 'terminate'
        result = self.sut.extract(str_val)
        
        expected = Verb(str_val, 'terminate', [VerbType.INTRANSITIVE, VerbType.TRANSITIVE], fake_conj)
        
        self.assertEqual(result, expected)
        self.assertEqual(self.lemmatizer.lemmatize.call_count, 1)
        self.assertEqual(self.conjugator.conjugate.call_count, 1)
    
    def test_verb_extractor_none(self):
        self.lemmatizer.lemmatize = MagicMock(return_value='X')
        fake_conj = VerbConjugations('a', 'b', 'c', 'd')
        self.conjugator.conjugate = MagicMock(return_value=fake_conj)
        str_val = 'X'

        result = self.sut.extract(str_val)
        
        expected = Verb(str_val, 'X', [VerbType.INTRANSITIVE, VerbType.TRANSITIVE, VerbType.LINKING], fake_conj)
        
        self.assertEqual(result, expected)
        self.assertEqual(self.lemmatizer.lemmatize.call_count, 1)
        self.assertEqual(self.conjugator.conjugate.call_count, 1)
    
    def test_verb_extractor_fail(self):
        self.lemmatizer.lemmatize = MagicMock(return_value=None)
        self.conjugator.conjugate = MagicMock(return_value=None)
        str_val = 'two words'

        with self.assertRaises(ValueError) as context:
            self.sut.extract(str_val)

        self.assertTrue('one word' in str(context.exception))

        self.assertEqual(self.lemmatizer.lemmatize.call_count, 0)
        self.assertEqual(self.conjugator.conjugate.call_count, 0)

if __name__ == '__main__':
    unittest.main()