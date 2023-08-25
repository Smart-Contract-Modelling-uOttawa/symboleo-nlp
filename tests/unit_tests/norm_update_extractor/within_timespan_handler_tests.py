import unittest
from unittest.mock import MagicMock

from app.classes.pattern_classes.pattern_variables import PatternVariable as PV
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.sym_point import Point
from app.classes.spec.point_function import TimeUnit, PointFunction
from app.classes.pattern_classes.within_timespan_event import WithinTimespanEvent
from app.classes.spec.predicate_function import  PredicateFunctionWHappensBefore
from app.classes.helpers.prop_maker import PropMaker
from app.classes.spec.norm import Obligation

from app.src.norm_update_extractor.handlers.within_timespan_handler import WithinTimespanHandler, IMapTimespan
from tests.helpers.sample_norm_lib import SampleNorms

class WithinTimespanEventHandlerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.timespan_mapper = IMapTimespan()
        self.sut = WithinTimespanHandler(self.timespan_mapper)

    def test_handler(self):
        self.timespan_mapper.map = MagicMock(return_value=('10', TimeUnit.Days))
        
        norm_config = SampleNorms.get_sample_obligation_config('test_id')
        pattern_class = WithinTimespanEvent({
            PV.TIMESPAN: '10 Days'
        })
        pattern_class.event = VariableEvent('evt_test')

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
                PredicateFunctionWHappensBefore(
                    VariableEvent('evt_action'),
                    Point(PointFunction(VariableEvent('evt_test'), 10, TimeUnit.Days))
                )
            )
        )
        self.assertEqual(new_norm, exp_norm)

if __name__ == '__main__':
    unittest.main()