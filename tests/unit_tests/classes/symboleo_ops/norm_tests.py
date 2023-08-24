import unittest
from unittest.mock import MagicMock

from app.classes.spec.norm import Norm, NormType
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.p_atoms import PAtom, PAtomPredicateTrueLiteral, PAtomPredicate

from app.classes.helpers.prop_maker import PropMaker

class NormTests(unittest.TestCase):
    def test_norm(self):
        norm = Norm(
            'norm_id', 
            None, 
            'debtor', 
            'creditor', 
            PropMaker.make_default(),
            PropMaker.make(
                PredicateFunctionHappens(VariableEvent('evt_test'))
            ),
            NormType.Obligation
            )

        trigger = norm.get_component('trigger')
        self.assertIsNone(trigger)
    
        antecedent = norm.get_component('antecedent')
        self.assertEqual(type(antecedent), PAtomPredicateTrueLiteral)

        consequent = norm.get_component('consequent')
        self.assertEqual(type(consequent), PAtomPredicate)

        with self.assertRaises(ValueError) as context:
            norm.get_component('x')
        self.assertTrue('Invalid component name' in str(context.exception))

        with self.assertRaises(ValueError) as context:
            norm.get_default_event('trigger')
        self.assertTrue('Default event not found' in str(context.exception))

        with self.assertRaises(ValueError) as context:
            norm.get_default_event('antecedent')
        self.assertTrue('Default event not found' in str(context.exception))
        
        cons_event = norm.get_default_event('consequent')
        self.assertEqual(cons_event, VariableEvent('evt_test'))



if __name__ == '__main__':
    unittest.main()