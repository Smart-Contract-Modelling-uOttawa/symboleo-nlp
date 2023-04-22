import unittest
from unittest.mock import MagicMock

from app.classes.custom_event.noun_phrase import NounPhrase
from app.classes.spec.declaration import Declaration

from app.src.sym_updaters.custom_event.asset_decl_extractor import AssetDeclarationExtractor
from app.src.sym_updaters.custom_event.asset_type_extractor import IExtractAssetType


class AssetDeclarationExtractorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.type_extractor = IExtractAssetType()
        self.sut = AssetDeclarationExtractor(self.type_extractor) 

    def test_asset_extractor(self):
        expected_value = Declaration('test', 'Test', 'assets', [])
        self.type_extractor.extract = MagicMock(return_value='Test')
        np = NounPhrase('test', 'test')
        result = self.sut.extract(np)
        self.assertEqual(result, expected_value)


    
if __name__ == '__main__':
    unittest.main()