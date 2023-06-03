import unittest
from unittest.mock import MagicMock
from app.classes.spec.sym_event import ContractEventName
from app.src.selection.element_extractors.contract_action_extractor import ContractActionExtractor

from app.src.selection.element_extractors.custom_event.verb.lemmatizer import ILemmatize

class ContractActionExtractorTests(unittest.TestCase):
    def setUp(self):
        self.lemmatizer = ILemmatize()
        self.lemmatizer.lemmatize = MagicMock(return_value = 'terminate')
        self.sut = ContractActionExtractor(self.lemmatizer)
    

    def test_contract_action_extractor(self):
        str_val = 'terminated'
        result = self.sut.extract(str_val)
        expected = ContractEventName.Terminated
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
