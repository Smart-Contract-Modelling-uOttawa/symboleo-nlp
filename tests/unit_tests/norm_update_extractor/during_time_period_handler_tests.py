import unittest
from unittest.mock import MagicMock

from app.classes.pattern_classes.pattern_variables import PatternVariable as PV
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.sym_point import Point, PointVDE
from app.classes.spec.sym_interval import Interval, IntervalFunction
from app.classes.pattern_classes.during_time_period import DuringTimePeriod
from app.classes.spec.predicate_function import PredicateFunctionHappensWithin
from app.classes.helpers.prop_maker import PropMaker
from app.classes.spec.norm import Obligation

from app.src.object_mappers.time_period_mapper import IMapTimePeriod, TimePeriod
from app.src.norm_update_extractor.handlers.during_time_period_handler import DuringTimePeriodHandler
from tests.helpers.sample_norm_lib import SampleNorms

class DuringTimePeriodHandlerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tp_mapper = IMapTimePeriod()

        self.sut = DuringTimePeriodHandler(self.tp_mapper)

    def test_handler(self):
        self.tp_mapper.map = MagicMock(return_value = TimePeriod('test_period'))

        norm_config = SampleNorms.get_sample_obligation_config('test_id')
        pattern_class = DuringTimePeriod({
            PV.TIME_PERIOD: 'test_period'
        })
        
        result = self.sut.handle(pattern_class, norm_config)
        
        new_norm: Obligation = result[0]
        self.assertEqual(len(result), 1)

        exp_norm = Obligation(
            'test_id',
            None,
            'debtor',
            'creditor',
            PropMaker.make_default(),
            PropMaker.make(
                PredicateFunctionHappensWithin(
                    VariableEvent('evt_action'),
                    Interval(
                        IntervalFunction(
                            PointVDE('test_period.start'),
                            PointVDE('test_period.end')
                        )
                    )
                )
            )
        )

        self.assertEqual(new_norm, exp_norm)

if __name__ == '__main__':
    unittest.main()