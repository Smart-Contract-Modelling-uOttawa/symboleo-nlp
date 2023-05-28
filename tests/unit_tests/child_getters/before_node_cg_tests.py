import unittest
from unittest.mock import MagicMock

from app.classes.elements.before_node import BeforeNode
from app.classes.custom_event.verb import Verb, VerbType, VerbConjugations

from app.src.child_getters.before_node import BeforeNodeCG
from app.src.child_getters.domain_timepoint_extractor import IExtractDomainTimePoints

class BeforeNodeCGTests(unittest.TestCase):
    def setUp(self):
        self.extractor = IExtractDomainTimePoints()
        self.extractor.extract = MagicMock(return_value = ['test'])
        self.sut = BeforeNodeCG(self.extractor)
    

    def test_verb_cg(self):
        test_val = BeforeNode()

        result = self.sut.get(None, None, test_val)
        self.assertEqual(len(result), 3)
        self.assertEqual(self.extractor.extract.call_count, 1)


if __name__ == '__main__':
    unittest.main()
