import unittest
from unittest.mock import MagicMock
from app.classes.spec.helpers import VariableDotExpression
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.primitive import ScoredPrimitive
from app.src.atom_assembler import IAssembleAtoms
from app.src.atom_extractor import AtomExtractor
from app.src.primitive_extractor import IExtractPrimitives
from tests.helpers.test_nlp import TestNLP

class AtomExtractorTests(unittest.TestCase):
    def setUp(self):
        options = { }
        self.nlp = TestNLP.get_nlp()
        
        self.primitive_extractor = IExtractPrimitives()
        self.fake_primitives = [ScoredPrimitive(VariableDotExpression('test'), 0.5)]
        self.primitive_extractor.extract = MagicMock(return_value = self.fake_primitives)
        
        self.atom_assembler = IAssembleAtoms()
        self.fake_atoms = [
            PredicateFunctionHappens(VariableEvent(VariableDotExpression('x')))
        ]
        self.atom_assembler.assemble = MagicMock(return_value = self.fake_atoms)

        self.sut = AtomExtractor(options, self.nlp, self.primitive_extractor, self.atom_assembler)

    def test_atom_extractor(self):
        sentence = 'this is a test'
        result = self.sut.extract(sentence)

        self.assertEqual(self.primitive_extractor.extract.call_count, 1)
        self.assertEqual(self.atom_assembler.assemble.call_count, 1)
        self.assertEqual(len(result), 1)

  
if __name__ == '__main__':
    unittest.main()