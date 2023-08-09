import unittest
from unittest.mock import MagicMock

from app.classes.spec.norm import Obligation
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.spec.p_atoms import PAtomPredicateTrueLiteral
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.domain_object import DomainEvent, DomainProp
from app.classes.spec.contract_spec_parameter import ContractSpecParameter
from app.classes.spec.declaration import Declaration, DeclarationProp
from app.classes.helpers.prop_maker import PropMaker
from app.classes.operations.contract_update_obj import ContractUpdateObj
from tests.helpers.test_contract import get_test_contract


class RunUpdateTests(unittest.TestCase):
    def test_run_update(self):
        contract = get_test_contract()

        init_num_parms = len(contract.contract_spec.parameters)

        test_proposition = PropMaker.make(PredicateFunctionHappens(VariableEvent('test_event')), True)
        new_norm = Obligation('new_ob', None, 'debtor', 'credit', PAtomPredicateTrueLiteral(), test_proposition)

        new_dm_obj = DomainEvent('NewEvent', [DomainProp('k', 'String')])

        new_decl = Declaration('test_decl', 'events', 'NewEvent', [ DeclarationProp('k', 'test_value', 'String')])

        new_parm = ContractSpecParameter('test_parm', 'String')

        update_obj = ContractUpdateObj(
            norms = [new_norm],
            domain_objects = [new_dm_obj],
            declarations = [new_decl],
            contract_parms = [new_parm]
        )

        contract.run_updates(update_obj)

        self.assertEqual(contract.contract_spec.obligations['new_ob'], new_norm)
        self.assertEqual(contract.contract_spec.declarations['test_decl'], new_decl)
        self.assertEqual(contract.domain_model.events['NewEvent'], new_dm_obj)
        self.assertEqual(contract.contract_spec.parameters[0], new_parm)


  
if __name__ == '__main__':
    unittest.main()