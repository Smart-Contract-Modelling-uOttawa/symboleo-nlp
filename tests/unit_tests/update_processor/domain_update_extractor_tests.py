import unittest
from unittest.mock import MagicMock

from app.classes.patterns.pattern import EventPattern, Pattern
from app.classes.spec.declaration import Declaration
from app.classes.spec.domain_object import DomainObject

from app.src.update_processor.domain_update_extractor import DomainUpdateExtractor
from app.src.sym_updaters.custom_event.asset_declaration_mapper import IMapAssetDeclarations
from app.src.sym_updaters.custom_event.event_declaration_mapper import IMapEventToDeclaration
from app.src.sym_updaters.custom_event.domain_model_mapper import IMapDeclarationToDomain

from tests.helpers.test_objects import CustomEvents

class DomainUpdateExtractorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.asset_decl_mapper = IMapAssetDeclarations()
        self.event_decl_mapper = IMapEventToDeclaration()
        self.domain_mapper = IMapDeclarationToDomain()
        self.sut = DomainUpdateExtractor(
            self.asset_decl_mapper,
            self.event_decl_mapper,
            self.domain_mapper
        )


    def test_domain_update_extractor(self):
        pattern = EventPattern()
        pattern.event = CustomEvents.paying()

        asset_decls = [
            Declaration('a1', 'A1', 'assets', []),
            Declaration('a2', 'A2', 'assets', [])
        ]
        self.asset_decl_mapper.map = MagicMock(return_value=asset_decls)

        event_decl = Declaration('evt_e1', 'E1', 'events', [])
        self.event_decl_mapper.map = MagicMock(return_value=event_decl)

        domain_obj = DomainObject('a', 'b', [])
        self.domain_mapper.map = MagicMock(return_value=domain_obj)

        result = self.sut.extract(pattern)

        self.assertEqual(len(result.declarations), 3)
        self.assertEqual(len(result.domain_objects), 3)
        self.assertEqual(result.declarations[2].name, 'evt_e1')
        self.assertEqual(self.asset_decl_mapper.map.call_count, 1)
        self.assertEqual(self.event_decl_mapper.map.call_count, 1)
        self.assertEqual(self.domain_mapper.map.call_count, 3)


    def test_domain_update_extractor_empty(self):
        pattern = Pattern()
        self.asset_decl_mapper.map = MagicMock(return_value=None)
        self.event_decl_mapper.map = MagicMock(return_value=None)
        self.domain_mapper.map = MagicMock(return_value=None)

        result = self.sut.extract(pattern)

        self.assertEqual(len(result.declarations), 0)
        self.assertEqual(len(result.domain_objects), 0)
        self.assertEqual(self.asset_decl_mapper.map.call_count, 0)
        self.assertEqual(self.event_decl_mapper.map.call_count, 0)
        self.assertEqual(self.domain_mapper.map.call_count, 0)


if __name__ == '__main__':
    unittest.main()