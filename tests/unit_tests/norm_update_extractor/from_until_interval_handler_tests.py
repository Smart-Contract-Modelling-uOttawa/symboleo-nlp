import unittest
from unittest.mock import MagicMock

from app.classes.pattern_classes.pattern_variables import PatternVariable as PV
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.sym_point import Point, PointVDE
from app.classes.spec.sym_interval import Interval, IntervalFunction
from app.classes.pattern_classes.from_until_interval import FromUntilInterval
from app.classes.spec.predicate_function import PredicateFunctionHappensWithin
from app.classes.helpers.prop_maker import PropMaker
from app.classes.spec.norm import Obligation

from app.src.norm_update_extractor.handlers.from_until_interval_handler import FromUntilIntervalHandler
from tests.helpers.sample_norm_lib import SampleNorms

class FromUntilIntervalHandlerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = FromUntilIntervalHandler()

    def test_handler(self):
        norm_config = SampleNorms.get_sample_obligation_config('test_id')
        pattern_class = FromUntilInterval({
            PV.TIMEPOINT: 'test_timepoint1',
            PV.TIMEPOINT2: 'test_timepoint2'
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
                            PointVDE('test_timepoint1'),
                            PointVDE('test_timepoint2')
                        )
                    )
                )
            )
        )

        self.assertEqual(new_norm, exp_norm)

if __name__ == '__main__':
    unittest.main()