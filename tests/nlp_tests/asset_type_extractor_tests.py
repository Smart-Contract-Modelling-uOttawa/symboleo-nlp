import unittest
from unittest.mock import MagicMock

from tests.helpers.test_nlp import TestNLP
from tests.helpers.test_contract import get_test_contract_for_assets

from app.src.custom_event_extractor.noun_phrase.asset_type_extractor import AssetTypeExtractor


test_suite = [
    ('$100', '$100', 'Money'),
    ('credit card', 'card', 'PaymentMethod'),
    ('Canada', 'Canada', 'Location'),
    ('pie', 'pie', 'Pie'),
    ('CAD', 'CAD', 'Currency'),
    ('March 30, 2024', 'March', 'Date'),
    ('authorization', 'authorization', 'Authorization'),
    ('pets', 'pets', 'Pets'),
]

class AssetTypeExtractorFullTests(unittest.TestCase):
    def setUp(self):
        nlp = TestNLP.get_nlp()
        self.sut = AssetTypeExtractor(nlp)

    def test_asset_type_extractor(self):
        contract = get_test_contract_for_assets()

        for test_val, head, exp_val in test_suite:
            res = self.sut.extract(test_val, head, contract)
            #print(res, exp_val)
            
            self.assertEqual(res, exp_val)

if __name__ == '__main__':
    unittest.main()