import unittest
from unittest.mock import MagicMock

from app.classes.spec.norm import Power, Obligation
from app.classes.spec.power_function import PFObligation, PFObligationName
from app.classes.spec.p_atoms import PAtomPredicateTrueLiteral
from app.classes.spec.predicate_function import PredicateFunction, PredicateFunctionHappens
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.prop_maker import PropMaker

from app.src.operations.norm_builder import NormBuilder


class NormBuilderTests(unittest.TestCase):
    def setUp(self):
        self.sut = NormBuilder()

    def test_suspension(self):
        prop = PropMaker.make(PredicateFunction())
        fake_norm = Obligation(
            'ob_test',
            None,
            'a',
            'b',
            PAtomPredicateTrueLiteral(),
            prop
        )
        
        fake_event = VariableEvent('evt_test')
        result = self.sut.build(fake_norm, fake_event)
        self.assertEqual(result.id, 'pow_suspend_ob_test')
        self.assertEqual(result.consequent.name, PFObligationName.Suspended)


    def test_resumption(self):
        fake_norm = Power(
            'pow_test', 
            None, 
            'debtor', 
            'creditor', 
            PAtomPredicateTrueLiteral(), 
            PFObligation(PFObligationName.Suspended, 'ob_test')
        )
        
        fake_event = VariableEvent('evt_test')
        result = self.sut.build(fake_norm, fake_event)

        self.assertEqual(result.id, 'pow_resume_ob_test')
        self.assertEqual(result.consequent.name, PFObligationName.Resumed)

    


if __name__ == '__main__':
    unittest.main()