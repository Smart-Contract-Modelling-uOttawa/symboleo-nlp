import unittest
from unittest.mock import MagicMock
from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.events.custom_event.noun_phrase import NounPhrase
from app.src.custom_event_extractor.noun_phrase.csp_noun_phrase_extractor import CspNounPhraseExtractor
from app.src.custom_event_extractor.element_extractor import IExtractElement

from tests.helpers.test_objects import NounPhrases

class CspNounPhraseExtractorTests(unittest.TestCase):
    def setUp(self):
        self.inner_extractor = IExtractElement[NounPhrase]()
        self.inner_extractor.extract = MagicMock(return_value=NounPhrases.apple_pie())

        self.sut = CspNounPhraseExtractor(self.inner_extractor)
    

    def test_csp_np_extractor(self):
        str_val = '[TEST_VALUE]'
        contract = ISymboleoContract()

        exp_val = NounPhrase('[TEST_VALUE]', '[TEST_VALUE]', asset_type='String', is_parm=True)

        result = self.sut.extract(str_val, contract)
        self.assertEqual(result, exp_val)
    
    def test_csp_np_extractor_num(self):
        str_val = '[TEST_AMOUNT]'
        contract = ISymboleoContract()

        exp_val = NounPhrase('[TEST_AMOUNT]', '[TEST_AMOUNT]', asset_type='Number', is_parm=True)

        result = self.sut.extract(str_val, contract)
        self.assertEqual(result, exp_val)
    
    def test_csp_np_extractor_skip(self):
        str_val = 'xxx'
        contract = ISymboleoContract()

        fallback = NounPhrases.apple_pie()
        self.inner_extractor.extract = MagicMock(return_value = fallback)

        result = self.sut.extract(str_val, contract)
        self.assertEqual(result, fallback)
    
if __name__ == '__main__':
    unittest.main()
