import unittest
from unittest.mock import MagicMock
from app.classes.spec.declaration import Declaration
from app.classes.spec.domain_object import DomainObject

from app.src.update_processor2.domain_updates.domain_update_extractor import DomainUpdateExtractor
from app.src.update_processor2.domain_updates.custom_event_extractor import IExtractCustomEvents
from app.src.update_processor2.domain_updates.asset_declaration_mapper import IMapAssetDeclarations
from app.src.update_processor2.domain_updates.event_declaration_mapper import IMapEventToDeclaration
from app.src.update_processor2.domain_updates.domain_model_mapper import IMapDeclarationToDomain

from tests.helpers.test_objects import CustomEvents

class DomainUpdateExtractorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.custom_event_extractor = IExtractCustomEvents()
        self.asset_decl_mapper = IMapAssetDeclarations()
        self.event_decl_mapper = IMapEventToDeclaration()
        self.domain_mapper = IMapDeclarationToDomain()
        self.sut = DomainUpdateExtractor(
            self.asset_decl_mapper,
            self.event_decl_mapper,
            self.domain_mapper,
            self.custom_event_extractor
        )


    def test_domain_update_extractor(self):
        self.custom_event_extractor.extract = MagicMock(return_value=CustomEvents.paying())

        asset_decls = [
            Declaration('a1', 'A1', 'assets', []),
            Declaration('a2', 'A2', 'assets', [])
        ]
        self.asset_decl_mapper.map = MagicMock(return_value=asset_decls)

        event_decl = Declaration('evt_e1', 'E1', 'events', [])
        self.event_decl_mapper.map = MagicMock(return_value=event_decl)

        domain_obj = DomainObject('a', 'b', [])
        self.domain_mapper.map = MagicMock(return_value=domain_obj)

        input_list = []

        result = self.sut.extract(input_list, None)

        self.assertEqual(len(result.declarations), 3)
        self.assertEqual(len(result.domain_objects), 3)
        self.assertEqual(result.declarations[2].name, 'evt_e1')
        self.assertEqual(self.custom_event_extractor.extract.call_count, 1)
        self.assertEqual(self.asset_decl_mapper.map.call_count, 1)
        self.assertEqual(self.event_decl_mapper.map.call_count, 1)
        self.assertEqual(self.domain_mapper.map.call_count, 3)


    def test_domain_update_extractor_empty(self):
        self.custom_event_extractor.extract = MagicMock(return_value=None)
        self.asset_decl_mapper.map = MagicMock(return_value=None)
        self.event_decl_mapper.map = MagicMock(return_value=None)
        self.domain_mapper.map = MagicMock(return_value=None)

        result = self.sut.extract([], None)

        self.assertEqual(len(result.declarations), 0)
        self.assertEqual(len(result.domain_objects), 0)
        self.assertEqual(self.custom_event_extractor.extract.call_count, 1)
        self.assertEqual(self.asset_decl_mapper.map.call_count, 0)
        self.assertEqual(self.event_decl_mapper.map.call_count, 0)
        self.assertEqual(self.domain_mapper.map.call_count, 0)


if __name__ == '__main__':
    unittest.main()