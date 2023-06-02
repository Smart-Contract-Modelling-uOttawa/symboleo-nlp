import unittest
from unittest.mock import MagicMock
from app.classes.spec.sym_event import ContractEventName
from app.src.selection.element_extractors.contract_action_extractor import ContractActionExtractor

class ContractActionExtractorTests(unittest.TestCase):
    def setUp(self):
        self.sut = ContractActionExtractor()
    

    def test_contract_action_extractor(self):
        str_val = 'terminated'
        result = self.sut.extract(str_val)
        expected = ContractEventName.Terminated
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
