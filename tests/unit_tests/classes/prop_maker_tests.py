import unittest
from unittest.mock import MagicMock
from typing import List, Tuple

from app.classes.helpers.prop_maker import PropMaker
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.spec.sym_event import VariableEvent


class PropMakerTests(unittest.TestCase):
    def setUp(self) -> None:
        x = 0
    
    def test_make(self):
        res = PropMaker.make(
            PredicateFunctionHappens(VariableEvent('evt_test'))
        )
        exp_sym = 'Happens(evt_test)'
        self.assertEqual(res.to_sym(), exp_sym)
    

    def test_make_multiple(self):
        res = PropMaker.make_multiple([
            (PredicateFunctionHappens(VariableEvent('evt_test1')), False),   
            (PredicateFunctionHappens(VariableEvent('evt_test2')), True)
        ])
        exp_sym = 'Happens(evt_test1) and not Happens(evt_test2)'
        self.assertEqual(res.to_sym(), exp_sym)
    
    
    def test_make_default(self):
        res = PropMaker.make_default()
        exp_sym = 'true'
        self.assertEqual(res.to_sym(), exp_sym)
    
    def test_make_not_assigned(self):
        res = PropMaker.make_not_assigned('a')

if __name__ == '__main__':
    unittest.main()