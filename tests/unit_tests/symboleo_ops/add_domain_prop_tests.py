import unittest
from unittest.mock import MagicMock

from app.classes.spec.domain_object import DomainProp
from tests.helpers.test_contract import get_test_contract


class AddDomainPropTests(unittest.TestCase):
    def test_domain_prop_adder(self):
        event_name = 'test_event' # Existing event on test contract
        new_prop = DomainProp('my_new_prop', 'str')
        contract = get_test_contract()

        contract.add_dm_prop(new_prop, 'events', event_name)
        target_prop = contract.domain_model.events['test_event'].props[0]
        self.assertEqual(target_prop.key, 'my_new_prop')


  
if __name__ == '__main__':
    unittest.main()