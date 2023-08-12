import unittest
from unittest.mock import MagicMock

from app.src.custom_event_extractor.noun_phrase.asset_type_extractor import AssetTypeExtractor
from app.src.custom_event_extractor.nlp.label_getter import IGetLabels

from tests.helpers.test_contract import get_test_contract

class AssetTypeExtractorTests(unittest.TestCase):
    def setUp(self):
        self.label_getter = IGetLabels()
        self.sut = AssetTypeExtractor(self.label_getter)
    
    def test_asset_type_extractor1(self):
        str_val = 'test_role'
        contract = get_test_contract()

        self.label_getter.get = MagicMock(return_value=None)

        result = self.sut.extract(str_val, str_val, contract)

        self.assertEqual(result, 'Role')
        self.assertEqual(self.label_getter.get.call_count, 0)
    
    def test_asset_type_extractor2(self):
        str_val = 'test_asset'
        contract = get_test_contract()

        self.label_getter.get = MagicMock(return_value=None)

        result = self.sut.extract(str_val, str_val, contract)

        self.assertEqual(result, 'TestAsset')
        self.assertEqual(self.label_getter.get.call_count, 0)
    
    def test_asset_type_extractor3(self):
        str_val = 'credit card'
        contract = get_test_contract()

        self.label_getter.get = MagicMock(return_value=None)

        result = self.sut.extract(str_val, 'card', contract)

        self.assertEqual(result, 'PaymentMethod')
        self.assertEqual(self.label_getter.get.call_count, 0)
    
    def test_asset_type_extractor4(self):
        str_val = '$100'
        contract = get_test_contract()

        self.label_getter.get = MagicMock(return_value=None)

        result = self.sut.extract(str_val, str_val, contract)

        self.assertEqual(result, 'Money')
        self.assertEqual(self.label_getter.get.call_count, 0)


    def test_asset_type_extractor5(self):
        str_val = 'test'
        contract = get_test_contract()

        self.label_getter.get = MagicMock(return_value='GPE')

        result = self.sut.extract(str_val, str_val, contract)

        self.assertEqual(result, 'Location')
        self.assertEqual(self.label_getter.get.call_count, 1)
    

    def test_asset_type_extractor6(self):
        str_val = 'nothing'
        contract = get_test_contract()

        self.label_getter.get = MagicMock(return_value=None)

        result = self.sut.extract(str_val, str_val, contract)

        self.assertEqual(result, 'Nothing')
        self.assertEqual(self.label_getter.get.call_count, 1)
    

if __name__ == '__main__':
    unittest.main()