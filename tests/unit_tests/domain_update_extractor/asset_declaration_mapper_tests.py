import unittest
from unittest.mock import MagicMock

from tests.helpers.test_objects import CustomEvents, AssetDeclarations
from tests.helpers.test_contract import get_test_contract

from app.src.domain_update_extractor.asset_declaration_extractor import IExtractAssetDeclarations
from app.src.domain_update_extractor.asset_declaration_mapper import AssetDeclarationMapper

class AssetDeclarationMapperTests(unittest.TestCase):
    def setUp(self) -> None:
        self.extractor = IExtractAssetDeclarations()
        self.sut = AssetDeclarationMapper(self.extractor)

    def test_asset_mapper1(self):
        # subj: legal_proceedings (extract)
        # no dobj
        # no pps
        evt = CustomEvents.legal_proceedings()
        contract = get_test_contract()
        fake_asset_decl = AssetDeclarations.legal_proceedings()
        self.extractor.extract = MagicMock(return_value=fake_asset_decl)

        results = self.sut.map(evt, contract)

        self.assertEqual(results, [fake_asset_decl])
        self.assertEqual(self.extractor.extract.call_count, 1)
    
    def test_asset_mapper2(self):
        # subj: role (ignore)
        # dobj: $100 (ignore)
        # pps: seller (role - ignore), credit card (payment method - include)
        evt = CustomEvents.paying()
        contract = get_test_contract()
        fake_asset_decl = AssetDeclarations.credit_card()
        self.extractor.extract = MagicMock(return_value=fake_asset_decl)

        results = self.sut.map(evt, contract)

        self.assertEqual(results[0], fake_asset_decl)
        self.assertEqual(self.extractor.extract.call_count, 1)
    

    def test_asset_mapper3(self):
        # subj: role
        # dobj: asset (pie)
        # pps: role
        evt = CustomEvents.eating_pie()
        contract = get_test_contract()
        fake_asset_decl = AssetDeclarations.pie()
        self.extractor.extract = MagicMock(return_value=fake_asset_decl)
        results = self.sut.map(evt, contract)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], fake_asset_decl)
        self.assertEqual(self.extractor.extract.call_count, 1)
    
if __name__ == '__main__':
    unittest.main()