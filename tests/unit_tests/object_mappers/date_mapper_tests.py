import unittest
from unittest.mock import MagicMock

from app.classes.spec.norm import Norm
from app.classes.spec.norm_config import NormConfig
from app.classes.pattern_classes.pattern_class import PatternClass, PatternVariable as PV
from app.classes.spec.sym_point import PointAtomContractEvent, PointVDE
from app.src.object_mappers.date_mapper import DateMapper

from tests.helpers.sample_norm_lib import SampleNorms

class DateMapperTests(unittest.TestCase):
    def setUp(self):
        self.sut = DateMapper()

    def test_date_mapper_parm(self):
        result = self.sut.map('[TEST_VALUE]', PV.DATE, None)
        self.assertEqual(result, 'test_value')
    
    def test_date_mapper_1(self):
        norm = SampleNorms.get_sample_norm('test_id')
        result = self.sut.map('x', PV.DATE, NormConfig(norm, None))
        self.assertEqual(result, 'test_id_date')

    def test_date_mapper_2(self):
        norm = SampleNorms.get_sample_norm('test_id')
        result = self.sut.map('x', PV.DATE2, NormConfig(norm, None))
        self.assertEqual(result, 'test_id_date2')
    
    def test_date_mapper_fail(self):
        norm = SampleNorms.get_sample_norm('test_id')
        
        with self.assertRaises(ValueError) as context:
            self.sut.map('x', PV.EVENT, NormConfig(norm, None))

        self.assertTrue('Pattern class is missing date' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
