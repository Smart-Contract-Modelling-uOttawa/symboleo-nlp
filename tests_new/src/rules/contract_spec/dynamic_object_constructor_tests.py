import unittest
from app.classes.graph.digraph import Digraph
from app.src.graph.graph_builder import GraphBuilder
from app.classes.spec.p_atoms import PAtom
from app.classes.graph.graph_node import test_graph
from app.classes.spec.helpers import TimeUnitStr, TimeValueInt
from app.classes.spec.sym_event import ObligationEvent, VariableEvent
from app.classes.spec.sym_point import PointAtomObligationEvent, Point, PointFunction, PointVDE
from app.classes.spec.sym_situation import ObligationState
from app.classes.spec.sym_interval import SituationExpression, Interval
from app.classes.spec.predicate_function import PredicateFunctionHappensWithin, PredicateFunctionHappens
from app.classes.processing.scored_components import ScoredComponent, ScoredType

from app.src.rules.contract_spec.dynamic_constructor import DynamicObjectConstructor

class DynamicObjectConstructorTests(unittest.TestCase):
    def setUp(self):
        graph_builder = GraphBuilder()
        self.graph = graph_builder.build(PAtom)
        #self.graph = Digraph(test_graph.values())
        self.sut = DynamicObjectConstructor(self.graph)

    def test_dynamic_object_constructor(self):
        test_suite = [
            (
                PointFunction,
                [PointVDE('test'), TimeValueInt(10), TimeUnitStr('days')],
                'PointFunction'
            ),
            (
                SituationExpression,
                [ObligationState('a', 'b')],
                'SituationExpression'
            ),
            (
                Interval,
                [SituationExpression(ObligationState('a', 'b'))],
                'Interval'
            ),
            (
                PointAtomObligationEvent,
                [ObligationEvent('a', 'b')],
                'PointAtomObligationEvent'
            ),
            (
                Point,
                [PointAtomObligationEvent(ObligationEvent('a','b'))],
                'Point'
            ),
            (
                PredicateFunctionHappensWithin,
                [VariableEvent('test'), Interval(SituationExpression(ObligationState('a','b')))],
                'PredicateFunctionHappensWithin'
            ),
            (
                PredicateFunctionHappens,
                [VariableEvent('test')],
                'PredicateFunctionHappens'
            )
        ]

        for pred_type, args, expected_type_str in test_suite:
            sp = ScoredType(pred_type, 1)
            sa = [ScoredComponent(a, 1) for a in args]
            result = self.sut.construct(sp, sa)
            self.assertEqual(type(result.obj).__name__, expected_type_str)

  
if __name__ == '__main__':
    unittest.main()