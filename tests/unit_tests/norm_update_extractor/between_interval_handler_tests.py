import unittest
from unittest.mock import MagicMock

from app.classes.pattern_classes.pattern_variables import PatternVariable as PV
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.sym_point import Point, PointVDE
from app.classes.spec.sym_interval import Interval, IntervalFunction
from app.classes.pattern_classes.between_interval import BetweenInterval
from app.classes.spec.predicate_function import PredicateFunctionHappensWithin
from app.classes.helpers.prop_maker import PropMaker
from app.classes.spec.norm import Obligation

from app.src.norm_update_extractor.handlers.between_interval_handler import BetweenIntervalHandler
from tests.helpers.sample_norm_lib import SampleNorms

class BetweenIntervalHandlerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = BetweenIntervalHandler()

    def test_handler(self):
        norm_config = SampleNorms.get_sample_obligation_config('test_id')
        pattern_class = BetweenInterval({
            PV.DATE: 'March 1, 2023',
            PV.DATE2: 'March 10, 2023'
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
                            PointVDE('March 1, 2023'),
                            PointVDE('March 10, 2023')
                        )
                    )
                )
            )
        )

        self.assertEqual(new_norm, exp_norm)

if __name__ == '__main__':
    unittest.main()