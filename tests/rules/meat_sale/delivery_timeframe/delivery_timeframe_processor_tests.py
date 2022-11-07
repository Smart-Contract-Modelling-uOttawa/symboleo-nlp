import unittest
from unittest.mock import MagicMock
from app.src.rules.meat_sale.delivery_timeframe.delivery_timeframe_processor import DeliveryTimeframeProcessor
from app.src.rules.meat_sale.delivery_timeframe.matchers import get_matcher
from tests.helpers.test_nlp import TestNLP

from app.classes.spec.helpers import VariableDotExpression
from app.classes.spec.predicate_function import PredicateFunctionHappens
from app.classes.spec.sym_event import VariableEvent

from app.classes.spec.symboleo_spec import PAtom
from app.src.graph.graph_builder import GraphBuilder
from app.src.dynamic_constructor import DynamicObjectConstructor

from .test_suite import test_suite

class DeliveryTimeframeProcessorTests(unittest.TestCase):
    def setUp(self):
        self.nlp = TestNLP.get_nlp()
        self.template = PredicateFunctionHappens(VariableEvent(VariableDotExpression('delivered')))
        self.matcher = get_matcher(self.nlp)
        graph_builder = GraphBuilder()
        digraph = graph_builder.build(PAtom)
        self.dynamic_constructor = DynamicObjectConstructor(digraph)

    def test_delivery_timeframe_processor(self):
        for t in test_suite:
            dtf = DeliveryTimeframeProcessor(self.template, self.matcher, self.nlp, self.dynamic_constructor)
            doc = self.nlp(t.sentence)
            results = dtf.process(doc)
            self.assertEqual(results[0].to_sym(), t.expected_sym)
  
if __name__ == '__main__':
    unittest.main()