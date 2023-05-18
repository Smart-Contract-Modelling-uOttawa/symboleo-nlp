import unittest
from unittest.mock import MagicMock

from tests.helpers.test_nlp import TestNLP
from app.src.extractors.custom_event.noun_phrase.asset_type_extractor import AssetTypeExtractor

test_suite = [
    ('$100', 'Money'),
    ('credit card', 'PaymentMethod'),
    ('Canada', 'Location'),
    ('pie', 'Other')
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
        for test_val, exp_val in test_suite:
            res = self.sut.extract(test_val)
            # res.print_me()
            # print('----')
            # exp_val.print_me()
            self.assertEqual(res, exp_val)

if __name__ == '__main__':
    unittest.main()