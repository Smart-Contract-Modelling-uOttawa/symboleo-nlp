import unittest
from unittest.mock import MagicMock

from app.classes.spec.norm import INorm
from app.classes.spec.norm_config import NormConfig, ParameterConfig
from app.classes.pattern_classes.all_pattern_classes import *

from app.src.operations.pattern_class_resolver import PatternClassResolver

from tests.helpers.sample_norm_lib import SampleNorms

class PatternClassResolverTests(unittest.TestCase):
    def setUp(self):
        self.sut = PatternClassResolver()

    def test_pattern_class_resolver_default(self):
        norm_config = NormConfig(INorm(), ParameterConfig('', '', '',[]))
        result = self.sut.resolve([BeforeDate(), AfterDate()], norm_config)

        self.assertTrue(isinstance(result, BeforeDate))
        

    def test_pattern_class_resolver_single(self):
        norm_config = NormConfig(INorm(), ParameterConfig('', '', ''))
        result = self.sut.resolve([BeforeDate()], norm_config)

        self.assertTrue(isinstance(result, BeforeDate))


    def test_pattern_class_resolver_cond(self):
        pcs = [
            AfterEvent(),
            CondAEvent()
        ]

        norm = SampleNorms.get_sample_norm('test_id')
        norm_config = NormConfig(norm, ParameterConfig('obligations', 'test_id', 'antecedent'))

        result = self.sut.resolve(pcs, norm_config)
        self.assertTrue(isinstance(result, CondAEvent))
    

    def test_pattern_class_resolver_after(self):
        pcs = [
            AfterEvent(),
            CondAEvent()
        ]

        norm = SampleNorms.get_sample_norm_with_ant('test_id')
        norm_config = NormConfig(norm, ParameterConfig('obligations', 'test_id', 'antecedent'))

        result = self.sut.resolve(pcs, norm_config)
        self.assertTrue(isinstance(result, AfterEvent))


if __name__ == '__main__':
    unittest.main()
