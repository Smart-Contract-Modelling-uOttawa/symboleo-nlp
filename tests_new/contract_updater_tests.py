import unittest
from unittest.mock import MagicMock

from app.src.rules.shared.interfaces import IProcessDocs
from app.src.processor_lookup import ILookupProcessor
from app.src.contract_updater import ContractUpdater

from app.classes.symboleo_contract import SymboleoContract
from app.classes.contract_update_request import ContractUpdateRequest
from tests.helpers.test_contract import get_test_contract


class ContractUpdaterTests(unittest.TestCase):
    def setUp(self):
        self.processor_lookup = ILookupProcessor
        fake_processor = IProcessDocs()
        fake_contract = get_test_contract()
        fake_processor.process = MagicMock(return_value = fake_contract)
        self.processor_lookup.lookup = MagicMock(return_value = [fake_processor])
        self.sut = ContractUpdater(self.processor_lookup)


    def test_contract_updater(self):
        test_contract = get_test_contract()
        init_sym = test_contract.to_sym()

        req = ContractUpdateRequest(test_contract, 'TEST_KEY', 'value', None)

        result = self.sut.update(req)

        self.assertEqual(type(result), SymboleoContract)
        self.assertEqual(self.processor_lookup.lookup.call_count, 1)
        self.assertEqual(test_contract.to_sym(), init_sym)
        

  
if __name__ == '__main__':
    unittest.main()