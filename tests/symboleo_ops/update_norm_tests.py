import unittest
from unittest.mock import MagicMock

from app.classes.spec.contract_spec import Obligation
from app.classes.spec.predicate_function import PredicateFunctionHappens, PredicateFunctionSHappensBefore
from app.classes.spec.p_atoms import PAtomPredicateTrueLiteral
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.sym_point import PointVDE
from app.classes.spec.prop_maker import PropMaker
from tests.helpers.test_contract import get_test_contract


class UpdateNormTests(unittest.TestCase):
    def test_update_norm(self):
        contract = get_test_contract()
        n1 = len(contract.contract_spec.obligations)
        expected_sym = 'new_ob: Obligation(debtor, credit, true, not SHappensBefore(test_event, test_point));'

        pred1 = PredicateFunctionHappens(VariableEvent('test_event'))
        prop1 = PropMaker.make(pred1, True)
        ob1 = Obligation('new_ob', None, 'debtor', 'credit', PAtomPredicateTrueLiteral(), prop1)
        contract.add_norm(ob1)

        self.assertEqual(len(contract.contract_spec.obligations), n1+1) 

        norm = contract.get_norm('new_ob', 'obligations')

        refinement = PredicateFunctionSHappensBefore(
            VariableEvent('test_event'),
            PointVDE('test_point')
        )
        norm.update('consequent', refinement)

        norm2 = contract.get_norm('new_ob', 'obligations')
        self.assertEqual(norm2.to_sym(), expected_sym)

  
if __name__ == '__main__':
    unittest.main()