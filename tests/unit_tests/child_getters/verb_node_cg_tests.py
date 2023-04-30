import unittest
from unittest.mock import MagicMock

from app.classes.selection.custom_event_node import VerbNode
from app.classes.custom_event.verb import Verb, VerbType, VerbConjugations

from app.src.child_getters.verb_node import VerbNodeCG

class VerbNodeCGTests(unittest.TestCase):
    def setUp(self):
        self.sut = VerbNodeCG()
    

    def test_verb_cg(self):
        test_verb = Verb('x', 'x', [VerbType.INTRANSITIVE, VerbType.LINKING, VerbType.TRANSITIVE], VerbConjugations('','','',''))
        test_val = VerbNode(test_verb)

        result = self.sut.get(None, None, test_val)
        self.assertEqual(len(result), 4)


if __name__ == '__main__':
    unittest.main()
