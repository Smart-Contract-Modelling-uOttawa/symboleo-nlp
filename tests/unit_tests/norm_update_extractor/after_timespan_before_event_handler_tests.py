import unittest
from unittest.mock import MagicMock

from app.classes.pattern_classes.pattern_variables import PatternVariable as PV
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.sym_point import Point
from app.classes.spec.point_function import TimeUnit, PointFunction
from app.classes.pattern_classes.after_timespan_before_event import AfterTimespanBeforeEvent
from app.classes.spec.predicate_function import PredicateFunctionHappensAfter
from app.classes.helpers.prop_maker import PropMaker
from app.classes.spec.norm import Obligation

from app.src.norm_update_extractor.handlers.after_timespan_before_event_handler import AfterTimespanBeforeEventHandler, IMapTimespan
from tests.helpers.sample_norm_lib import SampleNorms

class AfterTimespanBeforeEventHandlerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.timespan_mapper = IMapTimespan()
        self.sut = AfterTimespanBeforeEventHandler(self.timespan_mapper)

    def test_handler(self):
        self.timespan_mapper.map = MagicMock(return_value=('10', TimeUnit.Days))
        
        norm_config = SampleNorms.get_sample_obligation_config('test_id')
        pattern_class = AfterTimespanBeforeEvent({
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
                PredicateFunctionHappensAfter(
                    VariableEvent('evt_action'),
                    Point(PointFunction(VariableEvent('evt_test'), -10, TimeUnit.Days))
                )
            )
        )

        self.assertEqual(new_norm, exp_norm)

if __name__ == '__main__':
    unittest.main()