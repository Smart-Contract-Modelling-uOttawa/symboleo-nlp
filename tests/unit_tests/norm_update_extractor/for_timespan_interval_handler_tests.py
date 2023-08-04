import unittest
from unittest.mock import MagicMock

from app.classes.pattern_classes.pattern_variables import PatternVariable as PV
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.sym_point import Point, PointVDE
from app.classes.spec.point_function import TimeUnit, PointFunction
from app.classes.spec.sym_interval import Interval, IntervalFunction
from app.classes.pattern_classes.for_timespan_interval import ForTimespanInterval
from app.classes.spec.predicate_function import PredicateFunctionHappensWithin
from app.classes.helpers.prop_maker import PropMaker
from app.classes.spec.norm import Obligation

from app.src.norm_update_extractor.handlers.for_timespan_interval_handler import ForTimespanIntervalHandler
from tests.helpers.sample_norm_lib import SampleNorms

class DuringTimePeriodHandlerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = ForTimespanIntervalHandler()

    def test_handler(self):
        norm_config = SampleNorms.get_sample_obligation_config('test_id')
        pattern_class = ForTimespanInterval({
            PV.TIMEPOINT: 'test_timepoint',
            PV.TIMESPAN: '5 Days'
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
                            PointVDE('test_timepoint'),
                            PointFunction(PointVDE('test_timepoint'), 5, TimeUnit.Days)
                        )
                    )
                )
            )
        )

        self.assertEqual(new_norm, exp_norm)

if __name__ == '__main__':
    unittest.main()