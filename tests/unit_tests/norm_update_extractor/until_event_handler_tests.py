import unittest
from unittest.mock import MagicMock

from app.classes.pattern_classes.pattern_variables import PatternVariable as PV
from app.classes.spec.sym_event import VariableEvent
from app.classes.spec.sym_point import Point, PointVDE
from app.classes.pattern_classes.until_event import UntilEvent
from app.classes.spec.predicate_function import PredicateFunctionWHappensBeforeEvent
from app.classes.helpers.prop_maker import PropMaker
from app.classes.spec.norm import Obligation

from app.src.norm_update_extractor.handlers.until_event_handler import UntilEventHandler
from tests.helpers.sample_norm_lib import SampleNorms

class UntilEventHandlerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = UntilEventHandler()

    def test_handler_fail(self):
        norm_config = SampleNorms.get_sample_obligation_config('test_id', negation=False)
        pattern_class = UntilEvent()
        pattern_class.event = VariableEvent('evt_test')

        with self.assertRaises(ValueError) as context:
            self.sut.handle(pattern_class, norm_config)
        self.assertTrue('UntilEventHandler can only be used with a negated norm' in str(context.exception))
        

    def test_handler(self):
        norm_config = SampleNorms.get_sample_obligation_config('test_id', negation=True)
        pattern_class = UntilEvent()
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
                PredicateFunctionWHappensBeforeEvent(
                    VariableEvent('evt_action'),
                    VariableEvent('evt_test')
                ),
                negation=True
            )
        )
        self.assertEqual(new_norm, exp_norm)

if __name__ == '__main__':
    unittest.main()