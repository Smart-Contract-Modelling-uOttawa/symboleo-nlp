import unittest
from unittest.mock import MagicMock

from tests.nlp.test_objects import NounPhrases

from app.src.sym_updaters.custom_event.asset_type_extractor import AssetTypeExtractor


test_set = [
    (
        NounPhrases.legal_proceedings(),
        'String'
    ),
    (
        NounPhrases.hundred_dollars(),
        'Amount'
    )
    # (
    #     NounPhrases.credit_card(),
    #     'Method'
    # ),
    # (
    #     NounPhrases.pets(),
    #     'String'
    # )
]

class AssetTypeExtractorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = AssetTypeExtractor() # Will likely be injecting NLP/Framenet func in here

    def test_asset_extractor(self):
        # Will likely also be passing in CustomEvent for more context
        for np, expected_type in test_set:
            result = self.sut.extract(np)
            self.assertEqual(result, expected_type)

    
if __name__ == '__main__':
    unittest.main()