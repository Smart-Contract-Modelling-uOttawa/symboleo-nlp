import unittest
from unittest.mock import MagicMock

from app.classes.events.contract_events import ContractEvents, ContractEventName

class ContractEventTests(unittest.TestCase):
    
    def test_contract_event(self):
        x = ContractEvents.contract_event(ContractEventName.Terminated)
        self.assertEqual(x.verb.verb_str, 'terminate')

        x = ContractEvents.contract_event(ContractEventName.Activated)
        self.assertEqual(x.verb.verb_str, 'activate')


if __name__ == '__main__':
    unittest.main()