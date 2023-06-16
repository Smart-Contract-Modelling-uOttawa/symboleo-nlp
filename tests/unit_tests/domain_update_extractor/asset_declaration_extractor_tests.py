import unittest
from unittest.mock import MagicMock

from app.classes.events.custom_event.noun_phrase import NounPhrase
from app.classes.spec.declaration import Declaration

from app.src.domain_update_extractor.asset_declaration_extractor import AssetDeclarationExtractor


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