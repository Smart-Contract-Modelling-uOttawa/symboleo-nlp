import unittest
from unittest.mock import MagicMock

from typing import Dict
from app.classes.spec.domain_model import DomainModel, Role, Asset
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.declaration import Declaration
from tests.helpers.test_objects import NounPhrases
from tests.helpers.test_nlp import TestNLP
from tests.helpers.test_contract import get_test_contract_for_assets
from app.src.element_extractors.noun_phrase.noun_phrase_extractor import NounPhraseExtractor
from app.src.element_extractors.noun_phrase.asset_type_extractor import AssetTypeExtractor

test_suite = [
    ('apple pie', NounPhrases.apple_pie()),
    ('buyer', NounPhrases.buyer()),
    ('Canada', NounPhrases.canada()),
    ('credit card', NounPhrases.credit_card()),
    ('legal proceedings', NounPhrases.legal_proceedings()),
    ('property', NounPhrases.property()),
    ('pets', NounPhrases.pets()),
    ('renter', NounPhrases.renter()),
    ('the original digital photo files', NounPhrases.photos()),
    ('Dolphin', NounPhrases.dolphin()),
    ('$100', NounPhrases.hundred_dollars()),
    ('CAD', NounPhrases.cad()),

    ('client', NounPhrases.client()),
    ('contractor', NounPhrases.contractor()),
    ('services', NounPhrases.services()),
    ('disclosure', NounPhrases.disclosure()),

    
    ('CLIENT', NounPhrases.client_cap()),
    ('BOSCH', NounPhrases.bosch()),
    ('productivity', NounPhrases.productivity()),

]

# I can write some more tests that parse through this in much more detail, but not a priority
# In that case, I may also just build my own test contract and verify the proper values
# There may eventually be some NLP to verify as well
class NounPhraseExtractorTests(unittest.TestCase):
    def setUp(self):
        nlp = TestNLP.get_nlp()
        asset_type_extractor = AssetTypeExtractor(nlp)
        self.sut = NounPhraseExtractor(nlp, asset_type_extractor)

    def test_np_extractor(self):
        contract = get_test_contract_for_assets()

        for test_val, exp_val in test_suite:
            res = self.sut.extract(test_val, contract)
            # res.print_me()
            # print('----')
            # exp_val.print_me()
            self.assertEqual(res, exp_val)

if __name__ == '__main__':
    unittest.main()