import unittest
from unittest.mock import MagicMock

from typing import Dict
from app.classes.spec.domain_model import DomainModel, Role, Asset
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.declaration import Declaration
from tests.helpers.test_objects import NounPhrases
from tests.helpers.test_nlp import TestNLP
from app.src.extractors.custom_event.noun_phrase.noun_phrase_extractor import NounPhraseExtractor
from app.src.extractors.custom_event.noun_phrase.asset_type_extractor import AssetTypeExtractor

from app.src.extractors.custom_event.verb.lemmatizer import Lemmatizer

test_suite = [
    ('receiving', 'receive')
]

# I can write some more tests that parse through this in much more detail, but not a priority
# In that case, I may also just build my own test contract and verify the proper values
# There may eventually be some NLP to verify as well
class LemmatizerTests(unittest.TestCase):
    def setUp(self):
        nlp = TestNLP.get_nlp()
        self.sut = Lemmatizer(nlp)

    def test_lemmatizer(self):
        for test_val, exp_val in test_suite:
            res = self.sut.lemmatize(test_val)
            self.assertEqual(res, exp_val)

if __name__ == '__main__':
    unittest.main()