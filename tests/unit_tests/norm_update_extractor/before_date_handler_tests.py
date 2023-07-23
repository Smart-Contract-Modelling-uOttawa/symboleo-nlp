import unittest
from unittest.mock import MagicMock
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.sym_point import Point, PointVDE
from app.classes.pattern_classes.before_date import BeforeDate
from app.classes.spec.predicate_function import PredicateFunctionSHappensBefore
from app.classes.helpers.prop_maker import PropMaker
from app.classes.spec.norm import Obligation

from app.src.norm_update_extractor.handlers.before_date_handler import BeforeDateHandler
from tests.helpers.sample_norm_lib import SampleNorms

class BeforeDateHandlerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = BeforeDateHandler()

    def test_handler(self):
        norm_config = SampleNorms.get_sample_obligation_config('test_id')
        pattern_class = BeforeDate()
        pattern_class.date_text = 'March 30, 2024'

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
                PredicateFunctionSHappensBefore(
                    VariableEvent('evt_action'),
                    Point(PointVDE('"March 30, 2024"'))
                )
            )
        )
        self.assertEqual(new_norm, exp_norm)

if __name__ == '__main__':
    unittest.main()