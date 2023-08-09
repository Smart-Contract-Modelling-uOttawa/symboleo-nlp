import unittest
from unittest.mock import MagicMock

from tests.helpers.test_objects import CustomEvents, AssetDeclarations
from tests.helpers.test_contract import get_test_contract

from app.classes.pattern_classes.pattern_class import PatternClass, EventPatternClass
from app.classes.spec.declaration import EventDeclaration

from app.src.domain_update_extractor.declaration_mapper import DeclarationMapper
from app.src.domain_update_extractor.asset_declaration_mapper import IMapAssetDeclarations
from app.src.domain_update_extractor.event_declaration_mapper import IMapEventToDeclaration

class DeclarationMapperTests(unittest.TestCase):
    def setUp(self) -> None:
        self.asset_decl_mapper = IMapAssetDeclarations()
        self.event_decl_mapper = IMapEventToDeclaration()
        self.sut = DeclarationMapper(
            self.asset_decl_mapper,
            self.event_decl_mapper
        )

    def test_decl_mapper1(self):
        contract = get_test_contract()
        pattern_class = EventPatternClass()
        pattern_class.nl_event = CustomEvents.paying()

        fake_asset_decl = AssetDeclarations.legal_proceedings()
        self.asset_decl_mapper.map = MagicMock(return_value=[fake_asset_decl])
        self.event_decl_mapper.map = MagicMock(return_value=None)

        results = self.sut.map(pattern_class, contract, None)

        self.assertEqual(results, [fake_asset_decl])

        self.assertEqual(self.asset_decl_mapper.map.call_count, 1)
        self.assertEqual(self.event_decl_mapper.map.call_count, 1)
    
    def test_decl_mapper2(self):
        contract = get_test_contract()
        pattern_class = EventPatternClass()
        pattern_class.nl_event = CustomEvents.paying()

        fake_asset_decl = AssetDeclarations.legal_proceedings()
        self.asset_decl_mapper.map = MagicMock(return_value=[fake_asset_decl])

        fake_event_decl = EventDeclaration('evt_test', 'EvtTest')
        self.event_decl_mapper.map = MagicMock(return_value=fake_event_decl)

        results = self.sut.map(pattern_class, contract, None)

        self.assertEqual(results, [fake_asset_decl, fake_event_decl])

        self.assertEqual(self.asset_decl_mapper.map.call_count, 1)
        self.assertEqual(self.event_decl_mapper.map.call_count, 1)

    
    def test_decl_mapper_none(self):
        contract = get_test_contract()
        pattern_class = PatternClass()

        self.event_decl_mapper.map = MagicMock(return_value=None)
        self.asset_decl_mapper.map = MagicMock(return_value=[])

        results = self.sut.map(pattern_class, contract, None)

        self.assertEqual(len(results), 0)

        self.assertEqual(self.asset_decl_mapper.map.call_count, 0)
        self.assertEqual(self.event_decl_mapper.map.call_count, 0)

    

if __name__ == '__main__':
    unittest.main()