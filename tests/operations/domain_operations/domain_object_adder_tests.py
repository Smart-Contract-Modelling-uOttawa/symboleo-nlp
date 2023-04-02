import unittest
from unittest.mock import MagicMock
from app.classes.spec.proposition import PNegAtom
from app.classes.spec.p_atoms import PAtomPredicate
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.spec.declaration import Declaration, DeclarationProp
from app.classes.spec.contract_spec_other import ContractSpecParameter

from app.src.operations.domain_operations.dm_object_adder import DomainObjectAdder

from app.classes.spec.domain_model import DomainEvent, DomainProp

from tests.helpers.sample_norm_lib import SampleNorms

from tests.helpers.test_contract import get_test_contract

class DomainObjectAdderTests(unittest.TestCase):
    def setUp(self):
        self.sut = DomainObjectAdder()

    def test_add_declaration(self):
        contract = get_test_contract()
        init_events = len(contract.domain_model.events)

        new_obj = DomainEvent('Action', [DomainProp('k', 'String')])
        result = self.sut.add('events', contract, new_obj)
        
        ce = result.domain_model.events
        self.assertEqual(len(ce), init_events+1)
        self.assertEqual(ce['Action'].name, 'Action')

  
if __name__ == '__main__':
    unittest.main()