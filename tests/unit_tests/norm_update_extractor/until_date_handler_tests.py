import unittest
from unittest.mock import MagicMock

from app.classes.pattern_classes.pattern_variables import PatternVariable as PV
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.sym_point import Point, PointVDE
from app.classes.pattern_classes.until_date import UntilDate
from app.classes.spec.predicate_function import PredicateFunctionSHappensBefore
from app.classes.helpers.prop_maker import PropMaker
from app.classes.spec.norm import Obligation

from app.src.norm_update_extractor.handlers.until_date_handler import UntilDateHandler
from app.src.object_mappers.date_mapper import IMapDate
from tests.helpers.sample_norm_lib import SampleNorms

class UntilDateDateHandlerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.date_mapper = IMapDate()
        self.sut = UntilDateHandler(self.date_mapper)

    def test_handler_fail(self):
        self.date_mapper.map = MagicMock(return_value='test_date')
        norm_config = SampleNorms.get_sample_obligation_config('test_id', negation=False)
        pattern_class = UntilDate({
            PV.DATE: 'March 30, 2024'
        })

        with self.assertRaises(ValueError) as context:
            self.sut.handle(pattern_class, norm_config)
        self.assertTrue('UntilDateHandler can only be used with a negated norm' in str(context.exception))
        

    def test_handler(self):
        self.date_mapper.map = MagicMock(return_value='test_date')
        norm_config = SampleNorms.get_sample_obligation_config('test_id', negation=True)
        pattern_class = UntilDate({
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
                PredicateFunctionSHappensBefore(
                    VariableEvent('evt_action'),
                    Point(PointVDE('test_date'))
                ),
                negation=True
            )
        )
        self.assertEqual(new_norm, exp_norm)
        self.assertEqual(self.date_mapper.map.call_count, 1)

if __name__ == '__main__':
    unittest.main()