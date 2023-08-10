import unittest
from unittest.mock import MagicMock

from app.classes.pattern_classes.pattern_class import PatternClass, PatternVariable as PV

from app.src.object_mappers.time_period_mapper import TimePeriodMapper, TimePeriod

class TimePeriodMapperTests(unittest.TestCase):
    def setUp(self):
        self.sut = TimePeriodMapper()

    def test_time_period_mapper(self):
        pattern_class = PatternClass({
            PV.TIME_PERIOD: 'the contract period'
        })

        result = self.sut.map(pattern_class)

        exp_res = TimePeriod('self')
        self.assertEqual(result, exp_res)


if __name__ == '__main__':
    unittest.main()
