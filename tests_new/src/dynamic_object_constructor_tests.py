import unittest
from app.classes.graph.digraph import Digraph
from app.classes.graph.graph_node import test_graph
from app.classes.spec.helpers import VariableDotExpression
from app.classes.spec.sym_event import ObligationEvent
from app.classes.spec.sym_situation import ObligationState

from app.src.dynamic_constructor import DynamicObjectConstructor

class DynamicObjectConstructorTests(unittest.TestCase):
    def setUp(self):
        self.graph = Digraph(test_graph.values())
        self.sut = DynamicObjectConstructor(self.graph)

    def test_dynamic_object_constructor(self):
        arg_set = [
            ObligationState('a', 'b')
        ]
        situation_expression = self.sut.construct('SituationExpression', arg_set)
        self.assertEqual(type(situation_expression).__name__, 'SituationExpression')

        arg_set2 = [
            situation_expression
        ]
        interval = self.sut.construct('Interval', arg_set2)
        self.assertEqual(type(interval).__name__, 'Interval')

        arg_set3 = [
            ObligationEvent('a', 'b')
        ]
        paoe = self.sut.construct('PointAtomObligationEvent', arg_set3)
        self.assertEqual(type(paoe).__name__, 'PointAtomObligationEvent')

        arg_set4 = [
            paoe
        ]
        point = self.sut.construct('Point', arg_set4)
        self.assertEqual(type(point).__name__, 'Point')

        arg_set5 = [
            VariableDotExpression('x')
        ]
        ve = self.sut.construct('VariableEvent', arg_set5)
        self.assertEqual(type(ve).__name__, 'VariableEvent')

        arg_set6 = [
            ve,
            interval
        ]
        pfhw = self.sut.construct('PredicateFunctionHappensWithin', arg_set6) 
        self.assertEqual(type(pfhw).__name__, 'PredicateFunctionHappensWithin')

        arg_set7 = [
            ve
        ]
        pfhw = self.sut.construct('PredicateFunctionHappens', arg_set7) 
        self.assertEqual(type(pfhw).__name__, 'PredicateFunctionHappens')



    
  
if __name__ == '__main__':
    unittest.main()