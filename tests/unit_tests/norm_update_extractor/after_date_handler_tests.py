import unittest
from unittest.mock import MagicMock

from app.classes.pattern_classes.pattern_variables import PatternVariable as PV
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.sym_point import Point, PointVDE
from app.classes.pattern_classes.after_date import AfterDate
from app.classes.spec.predicate_function import PredicateFunctionHappensAfter
from app.classes.spec.norm_config import NormConfig, ParameterConfig
from app.classes.helpers.prop_maker import PropMaker
from app.classes.spec.norm import Obligation

from app.src.norm_update_extractor.handlers.after_date_handler import AfterDateHandler
from tests.helpers.sample_norm_lib import SampleNorms

class AfterDateDateHandlerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = AfterDateHandler()

    def test_handler(self):
        norm_config = SampleNorms.get_sample_obligation_config('test_id')
        pattern_class = AfterDate({
            PV.DATE: 'March 30, 2024'
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
                PredicateFunctionHappensAfter(
                    VariableEvent('evt_action'),
                    Point(PointVDE('"March 30, 2024"'))
                )
            )
        )
        self.assertEqual(new_norm, exp_norm)

if __name__ == '__main__':
    unittest.main()