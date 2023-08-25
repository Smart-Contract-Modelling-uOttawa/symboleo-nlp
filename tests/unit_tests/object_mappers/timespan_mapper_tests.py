import unittest
from unittest.mock import MagicMock

from app.classes.spec.sym_event import VariableEvent, ContractEvent, ContractEventName
from app.classes.pattern_classes.pattern_class import PatternClass, PatternVariable as PV
from app.classes.spec.sym_point import PointAtomContractEvent, PointVDE
from app.classes.spec.point_function import TimeUnit
from app.src.object_mappers.timespan_mapper import TimespanMapper

class TimespanMapperTests(unittest.TestCase):
    def setUp(self):
        self.sut = TimespanMapper()

    def test_timepoint_mapper(self):
        pattern_class = PatternClass({
            PV.TIMESPAN: '2 weeks'
        })
        result = self.sut.map(pattern_class)
        self.assertEqual(result, ('2', TimeUnit.Weeks))
    
    def test_timepoint_mapper_singular(self):
        pattern_class = PatternClass({
            PV.TIMESPAN: '1 week'
        })
        result = self.sut.map(pattern_class)
        self.assertEqual(result, ('1', TimeUnit.Weeks))
    
    def test_timepoint_mapper_fail(self):
        pattern_class = PatternClass({
            PV.TIMESPAN: '1 x'
        })
        with self.assertRaises(ValueError) as context:
            self.sut.map(pattern_class)

        self.assertTrue('Invalid Timespan' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
