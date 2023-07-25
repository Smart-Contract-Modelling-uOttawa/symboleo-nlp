import unittest
from unittest.mock import MagicMock
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.sym_point import Point
from app.classes.spec.point_function import TimeUnit, PointFunction
from app.classes.pattern_classes.timespan_before_event import TimespanBeforeEvent
from app.classes.spec.predicate_function import PredicateFunctionWHappensBefore
from app.classes.helpers.prop_maker import PropMaker
from app.classes.spec.norm import Obligation

from app.src.norm_update_extractor.handlers.timespan_before_event_handler import TimespanBeforeEventHandler
from tests.helpers.sample_norm_lib import SampleNorms

class TimespanBeforeEventHandlerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = TimespanBeforeEventHandler()

    def test_handler(self):
        norm_config = SampleNorms.get_sample_obligation_config('test_id')
        pattern_class = TimespanBeforeEvent()
        pattern_class.timespan_unit = TimeUnit.Days
        pattern_class.timespan_value = 10
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
                    Point(PointFunction(VariableEvent('evt_test'), -10, TimeUnit.Days))
                )
            )
        )
        self.assertEqual(new_norm, exp_norm)

if __name__ == '__main__':
    unittest.main()