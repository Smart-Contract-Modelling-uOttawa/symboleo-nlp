import unittest
from unittest.mock import MagicMock

from tests.helpers.sample_norm_lib import SampleNorms


class NegationExtractorTests(unittest.TestCase):

    def test_true(self):
        norm = SampleNorms.get_sample_obligation('test_id', True)
        result = norm.get_negation('consequent')
        self.assertTrue(result)
    

    def test_false(self):
        norm = SampleNorms.get_sample_obligation()
        result = norm.get_negation('consequent')
        self.assertFalse(result)

  
if __name__ == '__main__':
    unittest.main()