import unittest
from unittest.mock import MagicMock

from app.classes.custom_event.noun_phrase import NounPhrase
from app.classes.spec.declaration import Declaration

from app.src.sym_updaters.custom_event.asset_decl_extractor import AssetDeclarationExtractor


class AssetDeclarationExtractorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = AssetDeclarationExtractor() 

    def test_asset_extractor(self):
        expected_value = Declaration('test', 'Test', 'assets', [])
        np = NounPhrase('test', 'test', asset_type='Test')
        result = self.sut.extract(np)
        self.assertEqual(result, expected_value)

    
if __name__ == '__main__':
    unittest.main()