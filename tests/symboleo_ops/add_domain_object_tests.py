import unittest
from unittest.mock import MagicMock
from app.classes.spec.domain_model import DomainEvent, DomainProp
from tests.helpers.test_contract import get_test_contract

class AddDomainObjectTests(unittest.TestCase):
    def test_add_declaration(self):
        contract = get_test_contract()
        init_events = len(contract.domain_model.events)

        new_obj = DomainEvent('Action', [DomainProp('k', 'String')])
        contract.add_dm_object(new_obj)
        
        ce = contract.domain_model.events
        self.assertEqual(len(ce), init_events+1)
        self.assertEqual(ce['Action'].name, 'Action')

  
if __name__ == '__main__':
    unittest.main()