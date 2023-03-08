import unittest
from unittest.mock import MagicMock


from app.src.operations.configs import ParameterConfig
from app.src.operations.dm_prop_adder import DomainPropAdder

from app.classes.symboleo_contract import SymboleoContract
from app.classes.spec.domain_model import DomainProp
from tests.helpers.test_contract import get_test_contract


class DomainPropAdderTests(unittest.TestCase):
    def setUp(self):
        self.sut = DomainPropAdder()


    def test_domain_prop_adder(self):
        event_name = 'test_event' # Existing event on test contract
        config = ParameterConfig('', '', '', 'events', event_name)
        new_prop = DomainProp('my_new_prop','test_value', 'str')
        contract = get_test_contract()
        init_sym = contract.to_sym()

        result = self.sut.add(config, contract, new_prop)
        target_prop = result.domain_model.events['test_event'].props[0]
        self.assertEqual(target_prop.key, 'my_new_prop')
        self.assertEqual(target_prop.value, 'test_value')

        self.assertEqual(type(result), SymboleoContract)

        # Ensure init_contract has not changed
        self.assertEqual(contract.to_sym(), init_sym)
        

  
if __name__ == '__main__':
    unittest.main()