import unittest
from unittest.mock import MagicMock

from tests.helpers.test_objects import CustomEvents, AssetDeclarations
from tests.helpers.test_contract import get_test_contract_for_assets, get_test_contract

from app.src.update_processor.asset_declaration_extractor import IExtractAssetDeclarations
from app.src.update_processor.asset_declaration_mapper import AssetDeclarationMapper

# TODO: Should make a test suite
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
    
    @unittest.skip('FIX!')
    def test_asset_mapper2(self):
        # subj: role
        # dobj: $100 (extract)
        # pps: role, asset
        evt = CustomEvents.paying()
        contract = get_test_contract()
        fake_asset_decl1 = AssetDeclarations.hundred_dollars()
        fake_asset_decl2 = AssetDeclarations.credit_card()
        self.extractor.extract = MagicMock(side_effect=[fake_asset_decl1, fake_asset_decl2])

        results = self.sut.map(evt, contract)

        print(len(results))

        self.assertEqual(results, [fake_asset_decl1, fake_asset_decl2])

        self.assertEqual(self.extractor.extract.call_count, 2)
    
    @unittest.skip('FIX')
    def test_asset_mapper3(self):
        # subj: role
        # dobj: asset
        # pps: role, asset
        evt = CustomEvents.paying()
        contract = get_test_contract()
        existing_assets = [AssetDeclarations.hundred_dollars(), AssetDeclarations.credit_card()]
        self.extractor.extract = MagicMock(return_value=None)
        results = self.sut.map(evt, existing_assets)

        self.assertEqual(results, contract)
        self.assertEqual(self.extractor.extract.call_count, 0)
    
    @unittest.skip('FIX!')
    def test_asset_mapper4(self):
        # subj: proceedings(asset)
        # dobj: X
        # pps: property(asset), canada(extract)
        evt = CustomEvents.legal_proceedings_det()
        contract = get_test_contract_for_assets()
        #existing_assets = [AssetDeclarations.legal_proceedings(), AssetDeclarations.property()]

        fake_asset = AssetDeclarations.canada()
        self.extractor.extract = MagicMock(return_value=fake_asset)

        results = self.sut.map(evt, contract)

        self.assertEqual(results, [fake_asset]) 
        self.assertEqual(self.extractor.extract.call_count, 1)

    
if __name__ == '__main__':
    unittest.main()