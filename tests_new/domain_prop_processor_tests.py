import unittest
from unittest.mock import MagicMock

from app.src.rules.shared.configs import DomainPropProcessorConfig
from app.src.rules.shared.interfaces import IExtractProperties
from app.src.rules.shared.domain_prop_processor import DomainPropProcessor

from app.classes.symboleo_contract import SymboleoContract
from app.classes.contract_update_request import ContractUpdateRequest
from tests.helpers.test_contract import get_test_contract


class DomainPropProcessorTests(unittest.TestCase):
    def setUp(self):
        config = DomainPropProcessorConfig('events', 'test_event', 'test_prop', 'str')
        
        self.prop_extractor = IExtractProperties()
        fake_prop = 'test_prop_value'
        self.prop_extractor.extract = MagicMock(return_value=fake_prop)

        self.sut = DomainPropProcessor(config, self.prop_extractor)


    def test_contract_updater(self):
        test_contract = get_test_contract()
        init_sym = test_contract.to_sym()

        req = ContractUpdateRequest(test_contract, 'TEST_KEY', 'value', None)

        result = self.sut.process(req)

        target_prop = result.domain_model.events['test_event'].props[0]
        self.assertEqual(target_prop.key, 'test_prop')
        self.assertEqual(target_prop.value, 'test_prop_value')

        self.assertEqual(type(result), SymboleoContract)
        self.assertEqual(self.prop_extractor.extract.call_count, 1)

        # Ensure init_contract has not changed
        self.assertEqual(test_contract.to_sym(), init_sym)
        

  
if __name__ == '__main__':
    unittest.main()