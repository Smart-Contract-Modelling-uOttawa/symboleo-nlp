import unittest
from unittest.mock import MagicMock

from app.classes.selection.all_nodes import *
from app.classes.spec.norm import INorm
from app.classes.spec.domain_object import DomainEvent, Asset, DomainProp
from app.classes.spec.declaration import Declaration, DeclarationProp
from app.classes.spec.helpers import SpecHelpers

from app.src.updaters.new_event_node_updater_builder import NewEventNodeUpdaterBuilder

from tests.nlp.test_objects import FrameEvents

class FullNewEventNodeUpdaterTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = NewEventNodeUpdaterBuilder.build()

    def test_updater(self):
        norm = INorm()
        node = NewEventNode()
        value = FrameEvents.paying()

        result = self.sut.update_package(norm, node, value)

        expected_decls = [
            Declaration('$100', 'Amount', 'assets', []),
            Declaration('credit card', 'String', 'assets', []),
            Declaration('evt_pay', 'Pay', 'events', [
                DeclarationProp('paying_agent', 'buyer', 'Role'),
                DeclarationProp('pay_object', '$100', 'Amount'),
                DeclarationProp('paying_target', 'seller', 'Role'),
                DeclarationProp('pay_method', 'credit card', 'String'),
            ])
        ]

        expected_dmos = [
            Asset('Amount', []),
            Asset('String', []),
            DomainEvent('Pay', [
                DomainProp('paying_agent', 'Role'),
                DomainProp('pay_object', 'Amount'),
                DomainProp('paying_target', 'Role'),
                DomainProp('pay_method', 'String'),
            ])
        ]

        self.assertEqual(result.new_value.name, 'evt_pay')
        self.assertTrue(SpecHelpers.lists_eq(result.update_obj.declarations, expected_decls, 'name'))
        self.assertTrue(SpecHelpers.lists_eq(result.update_obj.domain_objects, expected_dmos, 'name'))


    

if __name__ == '__main__':
    unittest.main()