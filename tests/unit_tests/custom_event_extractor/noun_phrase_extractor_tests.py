import unittest
from unittest.mock import MagicMock
from app.classes.spec.symboleo_contract import ISymboleoContract
from app.classes.events.custom_event.noun_phrase import NounPhrase

from app.src.custom_event_extractor.noun_phrase.noun_phrase_extractor import NounPhraseExtractor
from app.src.custom_event_extractor.noun_phrase.asset_type_extractor import IExtractAssetType
from app.src.nlp.doc_parser import IParseDoc, NlpDoc, DocUnit

class NounPhraseExtractorTests(unittest.TestCase):
    def setUp(self):
        self.doc_parser = IParseDoc()
        self.asset_type_extractor = IExtractAssetType()
        self.sut = NounPhraseExtractor(self.doc_parser, self.asset_type_extractor)
    
    def test_np_extractor1(self):
        str_val = 'the original digital photo files'
        contract = ISymboleoContract()

        nlp_doc = NlpDoc([
            DocUnit('the', 'DT', 'det', 'files'),
            DocUnit('original', 'JJ', 'amod', 'files'),
            DocUnit('digital', 'JJ', 'amod', 'photo'),
            DocUnit('photo', 'NN', 'compound', 'files'),
            DocUnit('files', 'NNS', 'ROOT', 'files'),
        ])
        self.doc_parser.parse = MagicMock(return_value=nlp_doc)
        self.asset_type_extractor.extract = MagicMock(return_value='Files')

        exp_val = NounPhrase(
            str_val, 
            'files', 
            is_plural = True,
            is_role = False,
            det = 'the',
            adjs = ['original', 'digital', 'photo'],
            asset_type = 'Files',
            is_parm = False
        )

        result = self.sut.extract(str_val, contract)
        self.assertEqual(result, exp_val)
        self.assertEqual(self.asset_type_extractor.extract.call_count, 1)
        self.assertEqual(self.doc_parser.parse.call_count, 1)
    

    def test_np_extractor2(self):
        str_val = 'apple pie'
        contract = ISymboleoContract()

        nlp_doc = NlpDoc([
            DocUnit('apple', 'NN', 'compound', 'pie'),
            DocUnit('pie', 'NN', 'ROOT', 'pie'),
        ])
        self.doc_parser.parse = MagicMock(return_value=nlp_doc)
        self.asset_type_extractor.extract = MagicMock(return_value='Pie')
        
        exp_val = NounPhrase(
            str_val, 
            'pie', 
            is_plural = False,
            is_role = False,
            det = None,
            adjs = ['apple'],
            asset_type = 'Pie',
            is_parm = False
        )

        result = self.sut.extract(str_val, contract)
        self.assertEqual(result, exp_val)
        self.assertEqual(self.asset_type_extractor.extract.call_count, 1)
        self.assertEqual(self.doc_parser.parse.call_count, 1)
    
if __name__ == '__main__':
    unittest.main()
