import unittest
from unittest.mock import MagicMock

from tests.nlp.test_objects import FrameEvents, AssetDeclarations

from app.src.nlp.frame_event.asset_decl_extractor import IExtractAssetDeclarations
from app.src.nlp.frame_event.asset_declaration_mapper import AssetDeclarationMapper

class AssetDeclarationMapperTests(unittest.TestCase):
    def setUp(self) -> None:
        self.extractor = IExtractAssetDeclarations()
        self.sut = AssetDeclarationMapper(self.extractor)

    def test_asset_mapper1(self):
        # subj: legal_proceedings (extract)
        # no dobj
        # no pps
        evt = FrameEvents.legal_proceedings()
        existing_assets = []
        fake_asset_decl = AssetDeclarations.legal_proceedings()
        self.extractor.extract = MagicMock(return_value=fake_asset_decl)

        results = self.sut.map(evt, existing_assets)

        self.assertEqual(results, [fake_asset_decl])
        self.assertEqual(self.extractor.extract.call_count, 1)
    
    def test_asset_mapper2(self):
        # subj: role
        # dobj: $100 (extract)
        # pps: role, asset
        evt = FrameEvents.paying()
        fake_asset_decl1 = AssetDeclarations.hundred_dollars()
        fake_asset_decl2 = AssetDeclarations.credit_card()
        self.extractor.extract = MagicMock(side_effect=[fake_asset_decl1, fake_asset_decl2])

        results = self.sut.map(evt, [])

        self.assertEqual(results, [fake_asset_decl1, fake_asset_decl2])
        self.assertEqual(self.extractor.extract.call_count, 2)
    
    def test_asset_mapper3(self):
        # subj: role
        # dobj: asset
        # pps: role, asset
        evt = FrameEvents.paying()
        existing_assets = [AssetDeclarations.hundred_dollars(), AssetDeclarations.credit_card()]
        self.extractor.extract = MagicMock(return_value=None)
        results = self.sut.map(evt, existing_assets)

        self.assertEqual(results, [])
        self.assertEqual(self.extractor.extract.call_count, 0)
    
    def test_asset_mapper4(self):
        # subj: proceedings(asset)
        # dobj: X
        # pps: property(asset), canada(extract)
        evt = FrameEvents.legal_proceedings_det()
        existing_assets = [AssetDeclarations.legal_proceedings(), AssetDeclarations.property()]

        fake_asset = AssetDeclarations.canada()
        self.extractor.extract = MagicMock(return_value=fake_asset)

        results = self.sut.map(evt, existing_assets)

        self.assertEqual(results, [fake_asset]) 
        self.assertEqual(self.extractor.extract.call_count, 1)

    
if __name__ == '__main__':
    unittest.main()