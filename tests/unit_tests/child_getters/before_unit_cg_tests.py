import unittest
from unittest.mock import MagicMock

from app.classes.elements.static_elements import BeforeElement

from app.src.selection.child_getters.before_unit_cg import BeforeUnitCG
from app.src.selection.child_getters.domain_timepoint_extractor import IExtractDomainTimePoints

class BeforeUnitCGTests(unittest.TestCase):
    def setUp(self):
        self.extractor = IExtractDomainTimePoints()
        self.extractor.extract = MagicMock(return_value = ['test'])
        self.sut = BeforeUnitCG(self.extractor)
    

    def test_verb_cg(self):
        test_val = BeforeElement()

        result = self.sut.get(None, None, test_val)
        self.assertEqual(len(result), 3)
        self.assertEqual(self.extractor.extract.call_count, 1)


if __name__ == '__main__':
    unittest.main()
