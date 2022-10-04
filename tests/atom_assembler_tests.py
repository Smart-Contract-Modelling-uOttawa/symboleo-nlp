import unittest
from unittest.mock import MagicMock
from app.classes.spec.helpers import VariableDotExpression
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.spec.sym_event import VariableEvent
from app.src.atom_assembler import AtomAssembler
from app.src.predicate_builder import IBuildPredicates

class AtomAssemblerTests(unittest.TestCase):
    def setUp(self):
        self.predicate_builder = IBuildPredicates()
        self.fake_pred = PredicateFunctionHappens(VariableEvent(VariableDotExpression('test')))
        self.predicate_builder.build = MagicMock(side_effect = [self.fake_pred, None])

        self.candidates = ['a', 'b']
        self.sut = AtomAssembler(self.candidates, self.predicate_builder)

    def test_atom_assembler(self):
        primitives = [
            VariableDotExpression('x')
        ]
        result = self.sut.assemble(primitives)

        self.assertEqual(self.predicate_builder.build.call_count, 2)
        self.assertEqual(len(result), 1)
  
  
if __name__ == '__main__':
    unittest.main()