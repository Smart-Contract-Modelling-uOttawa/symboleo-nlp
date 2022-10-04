import unittest
from unittest.mock import MagicMock, call
from app.classes.spec.helpers import VariableDotExpression
from app.classes.spec.primitive import Primitive
from app.classes.spec.sym_situation import ObligationState, PowerState
from app.src.dynamic_constructor import IConstructDynamicObjects
from app.src.primitive_checker import ICheckPrimitives, PrimitiveChecker
from app.src.predicate_builder import PredicateBuilder
from tests.helpers.test_graph import TestGraph

class PrimitiveCheckerTests(unittest.TestCase):
    def setUp(self):
        self.sut = PrimitiveChecker()

    def test_primitive_checker(self):
        primitives = [
            VariableDotExpression('X'),
            ObligationState('a','b')
        ]

        r1: VariableDotExpression = self.sut.check('VariableDotExpression', primitives)
        self.assertEqual(r1.name, 'X')

        r2: ObligationState = self.sut.check('ObligationState', primitives)
        self.assertEqual(r2.obligation_variable, 'b')

        r3: PowerState = self.sut.check('PowerState', primitives)
        self.assertIsNone(r3)


    
  
if __name__ == '__main__':
    unittest.main()