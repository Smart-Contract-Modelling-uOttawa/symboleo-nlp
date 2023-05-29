import unittest
from unittest.mock import MagicMock

from tests.helpers.test_nlp import TestNLP
from tests.helpers.test_contract import get_test_contract_for_assets

from app.classes.spec.contract_spec import ContractSpec
from app.classes.spec.domain_model import DomainModel
from app.classes.spec.domain_object import DomainEnum
from app.classes.spec.symboleo_contract import SymboleoContract
from app.classes.spec.declaration import Declaration
from app.src.extractors.custom_event.noun_phrase.asset_type_extractor import AssetTypeExtractor


test_suite = [
    ('$100', '$100', 'Money'),
    ('credit card', 'card', 'PaymentMethod'),
    ('Canada', 'Canada', 'Location'),
    ('pie', 'pie', 'Pie'),
    ('CAD', 'CAD', 'Currency'),
    ('March 30, 2024', 'March', 'Date'),
]

# I can write some more tests that parse through this in much more detail, but not a priority
# In that case, I may also just build my own test contract and verify the proper values
# There may eventually be some NLP to verify as well
# TODO: May just want to add the roles/assets in here as well... If I do, it would be on the call, not the init
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