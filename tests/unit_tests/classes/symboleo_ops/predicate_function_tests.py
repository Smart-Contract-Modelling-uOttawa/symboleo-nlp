import unittest
from unittest.mock import MagicMock

from app.classes.spec.predicate_function import *
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.sym_point import Point, PointVDE
from app.classes.spec.sym_interval import Interval, IntervalFunction
from app.classes.spec.sym_situation import ContractState, ContractStateName

class PredicateFunctionTests(unittest.TestCase):
    def test_happens(self):
        p = PredicateFunctionHappens(VariableEvent('e'))
        res = p.to_sym()
        self.assertEqual(res, 'Happens(e)')
    
    def test_shappens_before(self):
        p = PredicateFunctionSHappensBefore(VariableEvent('e'), Point(PointVDE('p')))
        res = p.to_sym()
        self.assertEqual(res, 'ShappensBefore(e, p)')
    
    def test_shappens_before_event(self):
        p = PredicateFunctionSHappensBeforeEvent(VariableEvent('e1'), VariableEvent('e2'))
        q = PredicateFunctionSHappensBeforeEvent(VariableEvent('e1'), VariableEvent('e2'))
        res = p.to_sym()
        self.assertEqual(res, 'ShappensBeforeE(e1, e2)')
        self.assertEqual(p,q)
    
    def test_whappens_before(self):
        p = PredicateFunctionWHappensBefore(VariableEvent('e'), Point(PointVDE('p')))
        res = p.to_sym()
        self.assertEqual(res, 'WhappensBefore(e, p)')
    
    def test_whappens_before_event(self):
        p = PredicateFunctionWHappensBeforeEvent(VariableEvent('e1'), VariableEvent('e2'))
        res = p.to_sym()
        self.assertEqual(res, 'WhappensBeforeE(e1, e2)')
    
    def test_happens_after(self):
        p = PredicateFunctionHappensAfter(VariableEvent('e'), Point(PointVDE('p')))
        res = p.to_sym()
        self.assertEqual(res, 'HappensAfter(e, p)')
    
    def test_happens_within(self):
        p = PredicateFunctionHappensWithin(
            VariableEvent('e'), 
            Interval(IntervalFunction(PointVDE('p1'), PointVDE('p2')))
        )
        res = p.to_sym()
        self.assertEqual(res, 'HappensWithin(e, Interval(p1, p2))')
    
    def test_occurs(self):
        p = PredicateFunctionOccurs(
            ContractState(ContractStateName.Active),
            Interval(IntervalFunction(PointVDE('p1'), PointVDE('p2')))
        )
        q = PredicateFunctionOccurs(
            ContractState(ContractStateName.Active),
            Interval(IntervalFunction(PointVDE('p1'), PointVDE('p2')))
        )
        res = p.to_sym()
        self.assertEqual(res, 'Occurs(Active(self), Interval(p1, p2))')
        self.assertEqual(p,q)
    

    
  
if __name__ == '__main__':
    unittest.main()