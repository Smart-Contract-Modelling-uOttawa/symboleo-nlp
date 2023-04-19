import unittest
from unittest.mock import MagicMock

from app.classes.spec.norm import Obligation
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionWHappensBefore
from app.classes.spec.p_atoms import PAtomPredicateTrueLiteral
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.sym_point import PointVDE
from app.classes.spec.prop_maker import PropMaker
from tests.helpers.test_contract import get_test_contract


class UpdateNormTests(unittest.TestCase):
    def test_update_norm(self):
        contract = get_test_contract()
        obligation_count = len(contract.contract_spec.obligations)
        expected_sym = 'new_ob: Obligation(debtor, credit, true, not WhappensBefore(test_event, test_point));'

        # Construct obligation
        test_proposition = PropMaker.make(PredicateFunctionHappens(VariableEvent('test_event')), True)
        test_obligation = Obligation('new_ob', None, 'debtor', 'credit', PAtomPredicateTrueLiteral(), test_proposition)
        
        # Add the obligation
        contract.add_norm(test_obligation, 'new_ob', 'this is a test')
        self.assertEqual(len(contract.contract_spec.obligations), obligation_count + 1) 

        # Re-fetch the obligation
        refetched_obligation = contract.get_norm('new_ob', 'obligations')

        # Refine the obligation
        refinement = PredicateFunctionWHappensBefore(
            VariableEvent('test_event'),
            PointVDE('test_point')
        )
        refetched_obligation.update('consequent', refinement)

        # Verify the symboleo
        verified_norm = contract.get_norm('new_ob', 'obligations')
        self.assertEqual(verified_norm.to_sym(), expected_sym)

  
if __name__ == '__main__':
    unittest.main()