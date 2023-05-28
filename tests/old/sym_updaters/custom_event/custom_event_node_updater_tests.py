import unittest
from unittest.mock import MagicMock

from app.classes.elements.all_nodes import *
from app.classes.spec.norm import INorm
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.domain_object import DomainEvent, Asset
from app.classes.spec.declaration import Declaration

from app.src.sym_updaters.custom_event.custom_event_node_updater import CustomEventNodeUpdater

from app.src.sym_updaters.custom_event.asset_declaration_mapper import IMapAssetDeclarations
from app.src.sym_updaters.custom_event.event_declaration_mapper import IMapEventToDeclaration
from app.src.sym_updaters.custom_event.domain_model_mapper import IMapDeclarationToDomain

from tests.helpers.test_objects import CustomEvents

class CustomEventNodeUpdaterTests(unittest.TestCase):
    def setUp(self) -> None:
        self.asset_decl_mapper = IMapAssetDeclarations()
        self.event_decl_mapper = IMapEventToDeclaration()
        self.decl_domain_mapper = IMapDeclarationToDomain()
        self.sut = CustomEventNodeUpdater(
            self.asset_decl_mapper,
            self.event_decl_mapper,
            self.decl_domain_mapper
        )


    def test_updater(self):
        norm = INorm()
        node = CustomEventNode()
        value = CustomEvents.paying()

        asset_decls = [
            Declaration('a1', 'A1', 'assets', []),
            Declaration('a2', 'A2', 'assets', [])
        ]
        self.asset_decl_mapper.map = MagicMock(return_value=asset_decls)

        event_decl = Declaration('evt_e1', 'E1', 'events', [])
        self.event_decl_mapper.map = MagicMock(return_value=event_decl)

        dmos = [
            Asset('A1', []),
            Asset('A2', []),
            DomainEvent('E1', [])
        ]
        self.decl_domain_mapper.map = MagicMock(side_effect=dmos)

        result = self.sut.update_package(norm, node, value)

        self.assertEqual(len(result.update_obj.declarations), 3)
        self.assertEqual(len(result.update_obj.domain_objects), 3)
        self.assertEqual(type(result.new_value), VariableEvent)
        self.assertEqual(result.new_value.name, 'evt_e1')
        self.assertEqual(self.asset_decl_mapper.map.call_count, 1)
        self.assertEqual(self.event_decl_mapper.map.call_count, 1)
        self.assertEqual(self.decl_domain_mapper.map.call_count, 3)
    
    

if __name__ == '__main__':
    unittest.main()