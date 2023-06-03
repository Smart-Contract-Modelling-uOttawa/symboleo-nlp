import unittest
from unittest.mock import MagicMock
from app.classes.units.unit_type import UnitType
from app.classes.elements.custom_event_elements import VerbElement
from app.classes.events.custom_event.verb import Verb, VerbType, VerbConjugations

from app.src.selection.child_getters.verb_unit_cg import VerbUnitCG

class VerbNodeCGTests(unittest.TestCase):
    def setUp(self):
        self.sut = VerbUnitCG()
    

    def test_verb_cg_all(self):
        test_verb = Verb('x', 'x', [VerbType.INTRANSITIVE, VerbType.LINKING, VerbType.TRANSITIVE], VerbConjugations('','','',''))
        test_val = VerbElement(test_verb)

        result = self.sut.get(None, None, test_val)
        self.assertEqual(len(result), 4)
    
    
    def test_verb_cg_transitive(self):
        test_verb = Verb('x', 'x', [VerbType.TRANSITIVE], VerbConjugations('','','',''))
        test_val = VerbElement(test_verb)

        result = self.sut.get(None, None, test_val)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].unit_type, UnitType.DOBJ)
    
    
    def test_verb_cg_intransitive(self):
        test_verb = Verb('x', 'x', [VerbType.INTRANSITIVE], VerbConjugations('','','',''))
        test_val = VerbElement(test_verb)

        result = self.sut.get(None, None, test_val)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].unit_type, UnitType.ADVERB)
        self.assertEqual(result[1].unit_type, UnitType.FINAL_NODE)


    def test_verb_cg_linking(self):
        test_verb = Verb('x', 'x', [VerbType.LINKING], VerbConjugations('','','',''))
        test_val = VerbElement(test_verb)

        result = self.sut.get(None, None, test_val)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].unit_type, UnitType.PREDICATE)
    

    def test_verb_cg_none(self):
        test_verb = Verb('x', 'x', [], VerbConjugations('','','',''))
        test_val = VerbElement(test_verb)

        result = self.sut.get(None, None, test_val)
        self.assertEqual(len(result), 0)


if __name__ == '__main__':
    unittest.main()
